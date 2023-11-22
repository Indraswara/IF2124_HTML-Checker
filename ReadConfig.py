import json
from PDA import *
rawConfig = open("rulesPDA.txt", "r").read()
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
    print(symbols)

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
pda = PDA([], [], [], "Q", "Z0", transition)
pda.start("<html></html>")