from PDA import *
import re

RE = re.compile("/\\((\\w+)\\s+(\\w+)\\s+(\\w+)\\)\\s+=\\s+(\\w+)\\s+\\|\\s+(.+)/gm")
print(RE.match("(A B C) = A | A B C D"))

print(
)

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
    if line == "" or line.startswith("#"):
        continue

    matcher = re.match(r"\((\w+)\s+([\\\w]+)\s+(\w+)\)\s+=\s+(\w+)\s+\|\s?(.+)?", line)

    if matcher == None:
        continue
    
    print(matcher.groups())

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

    stack = matcher.group(5)
    if stack == None:
        stack = ""
    stack = stack.strip()
    if stack == "":
        stack = []
    else:
        stack = stack.strip().split(" ")
    rule.append((nextState, stack))

print(transition)

pda = PDA(statePDA, inputPDA, stackPDA, startState, startStack, transition)

pda.start("""
<html>
    <head>
    
    </head>
    <body>
    </body>
</html>
""")