class PDA:
    def __init__(self):
        self.states = set()
        self.input_symbols = set()
        self.stack_symbols = set()
        self.start_state = ''
        self.start_stack = ''
        self.accept_states = set()
        self.accept_empty = False
        self.transitions = {}

    def set_start_state(self, state):
        self.start_state = state

    def set_start_stack(self, stack_symbol):
        self.start_stack = stack_symbol

    def add_accept_state(self, state):
        self.accept_states.add(state)

    def add_input_symbol(self, symbol):
        self.input_symbols.add(symbol)

    def add_stack_symbol(self, symbol):
        self.stack_symbols.add(symbol)

    def add_transition(self, from_state, input_symbol, stack_symbol, to_state, stack_symbols_to_push):
        if (from_state, input_symbol, stack_symbol) not in self.transitions:
            self.transitions[(from_state, input_symbol, stack_symbol)] = []
        self.transitions[(from_state, input_symbol, stack_symbol)].append((to_state, stack_symbols_to_push))


    #unfinished
    def validate_input(self, input_string):
        stack = [self.start_stack]
        current_state = self.start_state
        index = 0

        while index < len(input_string) or stack:

            current_symbol = input_string[index] if index < len(input_string) else ''
            top_of_stack = stack[-1]

            
            transitions = self.transitions.get((current_state, current_symbol, top_of_stack), [])

            
            if not transitions and (current_state, '', top_of_stack) in self.transitions:
                transitions = self.transitions[(current_state, '', top_of_stack)]

            if not transitions:
                return False  

            next_state, stack_symbols_to_push = transitions[0]  

            stack.pop()  
            if stack_symbols_to_push != '':
                for symbol in stack_symbols_to_push[::-1]:
                    stack.append(symbol)  

            current_state = next_state
            if index < len(input_string): 
                index += 1

        return current_state in self.accept_states
    
pda = PDA()
pda.states = {'q', 'p'}
pda.input_symbols = {'0', '1'}
pda.stack_symbols = {'Z', 'X'}
pda.start_state = 'q'
pda.start_stack = 'Z'
pda.accept_states = {'p'}
pda.accept_empty = True

pda.add_transition('q', '0', 'Z', 'q', 'X')
pda.add_transition('q', '0', 'X', 'q', 'XX')
pda.add_transition('q', '1', 'X', 'q', 'X')
pda.add_transition('q', 'e', 'X', 'p', '')
pda.add_transition('p', 'e', 'X', 'p', '')
pda.add_transition('p', '1', 'X', 'p', 'XX')
pda.add_transition('p', '1', 'Z', 'p', '')

input_str = '010'
print(f"{input_str} is: " + str(pda.validate_input(input_str)))  
