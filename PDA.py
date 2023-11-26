from colorama import Fore, Style

StatePDA = str 
StackPDA = str
AlphabetPDA = str
InputPDA = str 

ID = tuple[StatePDA, InputPDA, list[StackPDA]]
FAIL = '\033[91m'
NORMAL = '\033[0m'

# Transition.get(state).get(input).get(stack) = {(state, stack)}
Transition = dict[StatePDA, dict[AlphabetPDA, dict[StackPDA, list[tuple[StatePDA, list[StackPDA]]]]]]
EPS = '\0'
class PDA: 
    ids: list[ID] = []

    def __init__ (self, startState:str, startStack: str, transition: Transition): 
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
        originalInput = input
        originalLen = len(input)
        self.ids.append((self.startState, input, [self.startStack]))
        count = len(input)

        lastParsedPositionFromBehind: int = 0

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
                    # break
                lastJobCount = len(self.ids)
                print()

            if len(self.ids) > maxJob:
                maxJob = len(self.ids)

            [state, input, stack] = self.ids.pop(0)
            lastParsedPositionFromBehind = len(input)

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

        if count:
            print(f"Character count\t\t\t: {count}")
            print(f"Iteration count\t\t\t: {count}")
            print(f"Itaration/Character Ratio\t: {(iteration * 100) // count}%")
            print(f"Maximum ID count\t\t: {maxJob}\n")

        if found:
            print(f"""{Fore.GREEN}
 █████╗  ██████╗ ██████╗███████╗██████╗ ████████╗███████╗██████╗ 
██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
███████║██║     ██║     █████╗  ██████╔╝   ██║   █████╗  ██║  ██║
██╔══██║██║     ██║     ██╔══╝  ██╔═══╝    ██║   ██╔══╝  ██║  ██║
██║  ██║╚██████╗╚██████╗███████╗██║        ██║   ███████╗██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚═╝        ╚═╝   ╚══════╝╚═════╝ 
        {Style.RESET_ALL}""")
        else:

            print(f"""{Fore.RED}
 ██▀███  ▓█████ ▄▄▄██▀▀▀▓█████  ▄████▄  ▄▄▄█████▓▓█████ ▓█████▄ 
▓██ ▒ ██▒▓█   ▀   ▒██   ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▓█   ▀ ▒██▀ ██▌
▓██ ░▄█ ▒▒███     ░██   ▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒███   ░██   █▌
▒██▀▀█▄  ▒▓█  ▄▓██▄██▓  ▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒▓█  ▄ ░▓█▄   ▌
░██▓ ▒██▒░▒████▒▓███▒   ░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░▒████▒░▒████▓ 
░ ▒▓ ░▒▓░░░ ▒░ ░▒▓▒▒░   ░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░░ ▒░ ░ ▒▒▓  ▒ 
  ░▒ ░ ▒░ ░ ░  ░▒ ░▒░    ░ ░  ░  ░  ▒       ░     ░ ░  ░ ░ ▒  ▒ 
  ░░   ░    ░   ░ ░ ░      ░   ░          ░         ░    ░ ░  ░ 
   ░        ░  ░░   ░      ░  ░░ ░                  ░  ░   ░    
                               ░                         ░      
            {Style.RESET_ALL}""")
            errorPoint = originalLen - lastParsedPositionFromBehind
            startLine = 0
            endLine = 0
            lineCount = 0
            for i in range(0, errorPoint):
                if originalInput[i] == '\n':
                    startLine = i
                    lineCount += 1
                
            for i in range(errorPoint, len(originalInput)):
                if originalInput[i] == '\n':
                    endLine = i
                    break

            errorLine = originalInput[startLine:endLine]
            print(FAIL + errorLine.strip() + NORMAL)
            print(f"Error at line {lineCount + 1}")
        
