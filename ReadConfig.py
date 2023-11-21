import json
from PDA import *
rawConfig = open("pda.config", "r").read()
lines = rawConfig.split("\n")

statePDA = lines.pop(0).split(" ")
inputPDA = lines.pop(0).split(" ")
stackPDA = lines.pop(0).split(" ")
startState = lines.pop(0)
startStack = lines.pop(0)
acceptingState = lines.pop(0).split(" ")
isAcceptingState = lines.pop(0)

transition: Transition = {}
for line in lines:
    symbols = line.split(" ")

    currentState = symbols.pop(0)
    currentInput = symbols.pop(0)
    if currentInput == "\\eps":
        currentInput = EPS
    currentStack = symbols.pop(0)

    nextState = symbols.pop(0)

    rule = transition
    if not currentState in rule:
        transition[currentState] = {}
    rule = transition[currentState]

    if not currentInput in rule:
        rule[currentInput] = {}
    rule = rule[currentInput]

    if not currentStack in rule:
        rule[currentStack] = []
    rule = rule[currentStack]

    rule.append((nextState, symbols))

print(json.dumps(transition, indent=2))
pda = PDA([], [], [], "q0", "Z0", transition)
pda.start("1111101010110101011111")