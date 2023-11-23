
StatePDA = str 
StackPDA = str
AlphabetPDA = str
InputPDA = str 

ID = tuple[StatePDA, InputPDA, list[StackPDA]]

# Transition.get(state).get(input).get(stack) = {(state, stack)}
Transition = dict[StatePDA, dict[AlphabetPDA, dict[StackPDA, list[tuple[StatePDA, list[StackPDA]]]]]]
EPS = '\0'
class PDA: 
    ids: list[ID] = []

    def __init__ (self, states: list[str], input: list[str], stack: list[str], startState:str, startStack: str, transition: Transition): 
        self.states = set(states)
        self.stack = set(stack)
        self.input = set(input)
        self.startState = startState  
        self.startStack = startStack
        self.transition = transition

    def pushJob(self, id: ID):
        [state, input, stack] = id
        for t in self.ids:
            [a, b, c] = t
            if state == a and input == b:
                match = True
                if len(stack) != len(c):
                    match = False
                else:
                    for [i, s] in enumerate(stack):
                        if s != c[i]:
                            match = False
                            break
                if match:
                    return
        self.ids.append(id)
    
    def start(self, input: InputPDA):
        found = False
        self.ids.append((self.startState, input, [self.startStack]))
        count = len(input)

        maxJob = 0
        iteration = 0
        lastJobCount = 0
        while len(self.ids) != 0:
            iteration += 1

            if False: 
                print(iteration)
                for [j, id] in enumerate(self.ids):
                    if j >= lastJobCount - 1:
                        print("<", end="")
                    if j == 0:
                        print(">", end="")
                    print("\t", end="")
                    print(j, id, end="")
                    print()
                    break
                lastJobCount = len(self.ids)
                print()

            if len(self.ids) > maxJob:
                maxJob = len(self.ids)

            [state, input, stack] = self.ids.pop(0)

            if len(stack) == 0:
                if len(input) == 0:
                    found = True
                    break
                continue

            headStack = stack.pop(0)
            tailStack = stack

            try:
                epsRules = self.transition.get(state).get(EPS).get(headStack) # type: ignore
                if epsRules == None:
                    raise Exception()

                for [nextState, nextStack] in epsRules:
                    self.pushJob((nextState, input, nextStack + tailStack))
            except:
                ...

            if len(input) == 0:
                continue

            headInput = input[0]
            tailInput = input[1:]

            try:
                rules = self.transition.get(state).get(headInput).get(headStack) # type: ignore
                if rules == None:
                    raise Exception()

                for [nextState, nextStack] in rules:
                    self.pushJob((nextState, tailInput, nextStack + tailStack))

            except:
                ...

            if headInput == headStack and headStack in self.input:
                self.pushJob((state, tailInput, tailStack))
        
        if found:
            print("Found")
        else:
            print("Not found")
        
        if count:
            print(count, iteration, f"{(iteration * 100) // count}%", maxJob)

