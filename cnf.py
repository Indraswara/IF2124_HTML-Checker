class CNF:
    # Kamus
    variables: list[str]
    terminals: list[str]
    productionRules: dict[str, list[list[str]]]
    startVariables: str

    def __init__(self, variables: list[str], terminals: list[str], productionRules: dict[str, list[list[str]]], startVariables: str) -> None:
        self.variables = variables
        self.terminals = terminals
        self.productionRules = productionRules
        self.startVariables = startVariables

        for variable in self.variables:
            if not variable in self.productionRules:
                self.productionRules[variable] = []


    def classifyUnitProduction(self, variable: str):
        unit: list[str] = []
        nonUnit: list[list[str]] = []
        for rule in self.productionRules[variable]:
            if len(rule) == 1 and rule[0] in self.variables:
                unit.append(rule[0])
            else:
                nonUnit.append(rule)

        return (unit, nonUnit)

    def printProductionRule(self):
        for variable in self.productionRules:
            for rule in self.productionRules[variable]:
                print(variable, "-->", rule)
    
    def eliminateUselessSymbol(self):
        generatingVariables: list[str] = []
        generatingSymbols: set[str] = set(self.terminals)

        while True:
            found = False
            for variable in self.variables:
                if not variable in generatingSymbols:
                    for rule in self.productionRules[variable]:
                        isGenerating = False
                        for symbol in rule:
                            if symbol in generatingSymbols:
                                isGenerating = True
                                break

                        if isGenerating:
                            generatingSymbols.add(variable)
                            generatingVariables.append(variable)
                            found = True

            if not found: 
                break

        generatingRules: dict[str, list[list[str]]] = {}
        for variable in generatingVariables:
            generatingRules[variable] = []
            for rule in self.productionRules[variable]:
                hasNonGenerating = False
                for symbol in rule:
                    if not symbol in generatingSymbols:
                        hasNonGenerating = True
                if not hasNonGenerating:
                    generatingRules[variable].append(rule)
        
        self.variables = generatingVariables
        self.productionRules = generatingRules


        usableTerminals: set[str] = set()
        usableVariables: dict[str, bool] = {}
        usableVariables[self.startVariables] = False

        while True:
            found = False
            for variable in usableVariables.copy():
                if usableVariables[variable] == True:
                    continue

                for rule in self.productionRules[variable]:
                    for symbol in rule:
                        if symbol in self.variables:
                            if not symbol in usableVariables:
                                usableVariables[symbol] = False
                                found = True
                        elif not symbol in usableTerminals:
                            usableTerminals.add(symbol)
                            found = True
                usableVariables[variable] = True

            if not found:
                break
        
        usableRules: dict[str, list[list[str]]] = {}
        for variable in usableVariables:
            usableRules[variable] = self.productionRules[variable]

        self.terminals = list(usableTerminals)
        self.variables = list(usableVariables)
        self.productionRules = usableRules

    def eliminateUnitProductionPair(self):
        result: dict[str, list[list[str]]] = {}
        unitProductionPair: dict[str, set[str]] = {}
        directUnitProduction: dict[str, set[str]] = {}
        directNonUnitProduction: dict[str, list[list[str]]] = {}

        for variable in self.variables:
            unitProductionPair[variable] = {variable}
            (unit, nonUnit) = self.classifyUnitProduction(variable)
            directUnitProduction[variable] = set(unit)
            directNonUnitProduction[variable] = nonUnit
            result[variable] = []

        for variable in self.productionRules:
            for rule in self.productionRules[variable]:
                if len(rule) == 1 and rule[0] in self.variables:
                    directUnitProduction[variable].add(rule[0])

        while True:
            found = False
            for first in unitProductionPair:
                for second in unitProductionPair[first].copy():
                    for directSecond in directUnitProduction[second]:
                        if not directSecond in unitProductionPair[first]:
                            unitProductionPair[first].add(directSecond)
                            found = True
            if not found:
                break

        
        for first in unitProductionPair:
            for second in unitProductionPair[first]:
                result[first] += directNonUnitProduction[second]

        self.productionRules = result

    def generatePermutation(self, s: list[str], target: set[str]) -> list[list[str]]:
        if len(s) == 0:
            return [[]]
        
        top = s[0]
        rest = s[1:]
        next = self.generatePermutation(rest, target)
        nextWith = list(map(lambda v: [top] + v, next))

        if top in target:
            return next + nextWith
        else:
            return nextWith
    
    def generateNotNullable(self, s: list[str], target: set[str]):
        permutation = self.generatePermutation(s, target)
        if permutation[0] == []:
            permutation.pop(0)
        return permutation

    def eliminateEpsilon(self):
        nullableVariables: set[str] = set()

        while True:
            found = False
            for variable in self.variables:
                if not variable in nullableVariables:
                    isNullable = False
                    for i, rule in enumerate(self.productionRules[variable]):
                        if len(rule) == 0:
                            isNullable = True
                            del self.productionRules[variable][i]
                            continue

                        hasNullable = True
                        for symbol in rule:
                            if not symbol in nullableVariables:
                                hasNullable = False
                        if hasNullable:
                            isNullable = True
                    

                    if isNullable:
                        nullableVariables.add(variable)
                        found = True
            if not found:
                break

        for variable in self.variables:
            l = len(self.productionRules[variable])
            for i in range(0, l):
                rule = self.productionRules[variable][i]
                hasNullable = False
                for symbol in rule:
                    if symbol in nullableVariables:
                        hasNullable = True
                
                if hasNullable:
                    newRules = self.generateNotNullable(rule, nullableVariables)

                    self.productionRules[variable][i] = newRules.pop()
                    for rule in newRules:
                        if not rule in self.productionRules[variable]:
                            self.productionRules[variable].append(rule)

    def eliminateMultipleRecursion(self):
        for variable in self.variables:
            newSymbol = "Base(" + variable + ")"
            found = False
            baseRule: list[list[str]] = []
            recurRule: list[list[str]] = []

            for rule in self.productionRules[variable]:
                if len(rule) > 1:
                    if rule[0] == variable:
                        rule[0] = newSymbol
                        recurRule.append(rule)
                        found = True
                        continue
                baseRule.append(rule)


            if found:
                self.productionRules[variable] = recurRule + [[newSymbol]]
                self.productionRules[newSymbol] = baseRule
                self.variables.append(newSymbol)

    def simplify(self):
        baseSymbol = "_"
        counter = 0

        terminalRules: dict[str, str] = {}

        for variable in self.productionRules:
            for rule in self.productionRules[variable]:
                if len(rule) > 1:
                    for symbol in rule:
                        if symbol in self.terminals and not symbol in terminalRules:
                            newSymbol = baseSymbol + str(counter)
                            terminalRules[symbol] = newSymbol
                            counter += 1
        
        for variable in self.productionRules:
            for rule in self.productionRules[variable]:
                for i in range(0, len(rule)):
                    if rule[i] in terminalRules:
                        rule[i] = terminalRules[rule[i]]

        for terminal in terminalRules:
            self.productionRules[terminalRules[terminal]] = [[terminal]]

        variableRules: dict[str, str] = {}

        for variable in self.productionRules:
            for rule in self.productionRules[variable]:
                l = len(rule)
                if l > 2:
                    for i in range(l - 2, 0, -1):
                        combinedVariable = rule[i] + "\3" + rule[i + 1]
                        if not combinedVariable in variableRules:
                            newSymbol = baseSymbol + str(counter)
                            counter += 1
                            variableRules[combinedVariable] = newSymbol
                            rule[i] = newSymbol
                            rule.pop()
                        else:
                            rule[i] = variableRules[combinedVariable]
                            rule.pop()

        for variable in variableRules:
            target = variableRules[variable]
            self.productionRules[target] = [variable.split("\3")]



# cnf = CNF(["S", "A", "B"], ["a", "b"], {
#     "S": [["A", "B"]],
#     "A": [["a", "A", "A"], []],
#     "B": [["b", "B", "B"], []]
# }, "P")

# #cnf.eliminateEpsilon()
# cnf.eliminateEpsilon()

# cnf = CNF(['I', 'F', 'T', 'E', 'H'], ['a', 'b', '0', '1', '(', ')', '*', '+'], {
#     'I' : [['a'], ['b'], ['I', 'a'], ['I', 'b'], ['I', '0'], ['I', '1']],
#     'F' : [['I'], ['(', 'E', ')']],
#     'T' : [['F'], ['T', '*', 'F']],
#     'E' : [['T'], ['E', '+', 'T'], ['H', 'E']],
# }, 'E') 

# cnf = CNF(['S', 'A', 'B'], ['a', 'b'], {
#     'S': [['A', 'B'], ['a']],
#     'A': [['b']]
# }, 'S')

# cnf = CNF([
#     'Html',
#     'Head',
#     'Body',
#     'Title',
#     'Link',
#     'Script',
#     'H1', 'H2', 'H3', 'H4', 'H5', 'H6',
#     'P',
#     'Br',
#     'Em',
#     'B',
#     'Abbr',
#     'Strong',
#     'Small',
#     'Hr',
#     'Div',
#     'A',
#     'Img',
#     'Button',
#     'Form',
#     'Input',
#     'Table',
#     'Tr',
#     'Td',
#     'Th',
#     'Komentar'
# ], 
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '<', '>', '/'], 
# {
#     'Html': [['<', 'h', 't', 'm', 'l', '>', 'Head', 'Body', '<', '/', 'h', 't', 'm', 'l', '>']],
#     'Head': [['<', 'h', 'e', 'a', 'd', '>', 'Title', '<', '/', 'h', 'e', 'a', 'd', '>']],
#     'Body': [['<' , 'b', 'o', 'd', 'y', '>', '<', '/', 'b', 'o', 'd', 'y', '>']],
#     'Title': [['t']]
# }, 'Html')

# cnf.eliminateUselessSymbol()
# cnf.eliminateUnitProductionPair()
# cnf.simplify()
# cnf.printProductionRule()
# print(cnf.terminals, cnf.variables)