start_input = ""
found = False 
accepted_config = [] 


productions = {}


acceptable_states = []


accept_with = ""

def generate(state, input_str, stack, config):
    global productions, found

    if found:
        return False

    if is_found(state, input_str, stack):
        found = True
        accepted_config.extend(config)
        return True

    moves = get_moves(state, input_str, stack, config)
    if not moves:
        return False

    for move in moves:
        if generate(move[0], move[1], move[2], config + [(move[0], move[1], move[2])]):
            return True

    return False

def get_moves(state, input_str, stack, config):
    global productions

    moves = []

    for prod_state, prod_rules in productions.items():
        if prod_state != state:
            continue

        for rule in prod_rules:
            current = rule
            new = []

            new.append(current[3])

            if len(current[0]) > 0:
                if len(input_str) > 0 and input_str[0] == current[0]:
                    new.append(input_str[1:])
                else:
                    continue
            else:
                new.append(input_str)

            if len(current[1]) > 0:
                if len(stack) > 0 and stack[0] == current[1]:
                    new.append(current[2] + stack[1:])
                else:
                    continue
            else:
                new.append(current[2] + stack)

            moves.append(new)

    return moves


def is_found(state, input_str, stack):
    global accept_with, acceptable_states

    if len(input_str) > 0:
        return False

    if accept_with == "E":
        if len(stack) < 1:
            return True
        return False
    else:
        if state in acceptable_states:
            return True
        return False

def parse_file(filename):
    global productions, start_symbol, start_stack, acceptable_states, accept_with

    try:
        with open(filename) as file:
            lines = [line.rstrip() for line in file]

    except FileNotFoundError:
        return False

    start_symbol = lines[3]
    start_stack = lines[4]
    acceptable_states.extend(lines[5].split())
    accept_with = lines[6]

    for line in lines[7:]:
        production = line.split()
        configuration = [(production[1], production[2], production[4], production[3])]

        if production[0] not in productions:
            productions[production[0]] = []

        configuration = [tuple(s if s != "e" else "" for s in tup) for tup in configuration]
        productions[production[0]].extend(configuration)

    return True


def done():
    if found:
        print(f"Hurray! Input word \"{start_input}\" is part of the grammar.")
    else:
        print(f"Sorry! Input word \"{start_input}\" is not part of the grammar.")

def print_config(config):
    for i in config:
        print(i)

filename = input("Please enter your automata file:\n")
while not parse_file(filename):
    print("File not found!")
    filename = input("Please enter your automata file again:\n")
print("Automata built.")

start_input = input("Please enter your word:\n")
print(f"Checking word \"{start_input}\" ...")

while start_input != "end":
    if not generate(start_symbol, start_input, start_stack, [(start_symbol, start_input, start_stack)]):
        done()
    else:
        print_config(accepted_config)
        done()

    start_input = input("Enter your next word (or end):\n")
    print(f"Checking word \"{start_input}\" ...")
