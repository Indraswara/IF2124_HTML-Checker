
StatePDA = str 
StackPDA = str
AlphabetPDA = str
InputPDA = str 

ID: tuple[list[StatePDA], InputPDA, list[StackPDA]]
Transition: dict[StatePDA, dict[AlphabetPDA, dict[StackPDA, list[tuple[StatePDA, StackPDA]]]]]
# (State, input, stack) 
eps = '\0'

transition: Transition = {
    "p": {
        "0": {
            "0": [("p", "0")],
            "1": [("p", "1")],
            "z": [("p", "0")]
        },
        "1": {
            "1": [("p", "1")],
            "0": [("p", "0")],
            "z": [("p", "1")]
        },
        eps: {
            eps: [("q", "z")]
        }
    },
    "q": {
        "0": {
            "0": [("0", eps)]
        },
        "1": {
            "1": [("1", eps)]
        },
        "": {
            "": [("", "z")]
        }
    }
}

class PDA: 
    startID: ID = []

    def _init_ (self, states: list[str], input: list[str], stack: list[str], start_state:str, accept_empty: bool, transitions: Transition): 
        self.states = states 
        self.stack = stack 
        self.start_state = start_state  
        self.accept_empty = accept_empty

    def process(startID, transition):
        ...