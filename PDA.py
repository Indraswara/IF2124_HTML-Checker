
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
        self.states = states 
        self.stack = stack 
        self.input = input
        self.startState = startState  
        self.startStack = startStack
        self.transition = transition
    
    def start(self, input: InputPDA):
        self.ids.append((self.startState, input, [self.startStack]))
        self.process()
    
    def process(self):
        found = False

        while len(self.ids) != 0:
            [state, input, stack] = self.ids.pop(0)

            if len(stack) == 0:
                if len(input) == 0:
                    found = True
                continue

            headStack = stack.pop(0)
            tailStack = stack

            try:
                epsRules = self.transition.get(state).get(EPS).get(headStack) # type: ignore
                if epsRules == None:
                    raise Exception()

                for [nextState, nextStack] in epsRules:
                    self.ids.append((nextState, input, nextStack + tailStack))
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
                    self.ids.append((nextState, tailInput, nextStack + tailStack))

            except:
                ...
        
        if found:
            print("Found")
        else:
            print("Not found")

