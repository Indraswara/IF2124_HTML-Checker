from PDA import *
import re

def parsePDAConfig(raw: str) -> tuple[StatePDA, StackPDA, Transition]:
    rawConfig = open("pda.txt", "r").read()
    lines = rawConfig.split("\n")

    [startState, startStack] = lines.pop(0).split(" ")
    transition: Transition = {}

    for line in lines:
        if line == "" or line.startswith("#"):
            continue

        matcher = re.match(r"\((\\?\$?\w+)\s+([^\s]+)\s+([^\s]+)\)\s+=\s+(\\?\$?\w+)\s+\|\s?(.+)?", line)

        if matcher == None:
            continue
        
        # print(matcher.groups())

        currentState = matcher.group(1)
        currentInput = matcher.group(2)
        if currentInput == "\\eps":
            currentInput = EPS
        elif currentInput == "\\space":
            currentInput = " "
        elif currentInput == "\\newline":
            currentInput = "\n"
        currentStack = matcher.group(3)

        nextState = matcher.group(4)

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

        rawStack = matcher.group(5)
        if rawStack == None:
            rawStack = ""
        rawStack = rawStack.strip()

        nextStack: list[str] = []
        if rawStack == "":
            nextStack = []
        else:
            nextStack = rawStack.strip().split(" ")
        
        rule.append((nextState, nextStack))
    
    return (startState, startStack, transition)