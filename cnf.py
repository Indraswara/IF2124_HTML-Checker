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
    
    # def hasEpsilonProduction(variable: str):
    #     pass

    # def findUnitProductionPair(self) -> dict[str,set[str]]:
    #     result: dict[str,set[str]] = {}
    #     for variable in self.productionRules:
    #         result[variable] = variable

    #     foundNew = True
    #     while foundNew:
    #         foundNew = False
    #         for unitProduction in result:
                

    #     print(result)



cnf = CNF(["I", "F", "T", "E"], ["a", "b"], {
    "I" : [["a"], ["b"], ["I", "a"], ["I", "b"], ["I", "0"], ["I", "1"]],
    "F" : [["I"], ["(", "E", ")"]],
    "T" : [["F"], ["T", "*", "F"]],
    "E" : [["T"], ["E", "+", "T"]],
}, "E") 


cnf.findUnitProductionPair()





# for rule in self.productionRules[variable]:
            #     if len(rule) == 1 and rule[0] in self.variables:
            #         res.append((variable, rule[0]))