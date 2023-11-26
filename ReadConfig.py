from PDA import *
import re

rawConfig = open("pdaRules-indra.config", "r").read()
lines = rawConfig.split("\n")

statePDA = lines.pop(0).split(" ")
inputPDA = lines.pop(0).split(" ")
stackPDA = lines.pop(0).split(" ")
startState = lines.pop(0)
startStack = lines.pop(0)
acceptingState = lines.pop(0).split(" ")
isAcceptingState = lines.pop(0)

transition: Transition = {}
closure: list[tuple[StatePDA, InputPDA, StackPDA, StatePDA, list[StackPDA]]] = []
for line in lines:
    if line == "" or line.startswith("#"):
        continue

    matcher = re.match(r"\((\\?\$?\w+)\s+([^\s]+)\s+(\\?\$?\w+)\)\s+=\s+(\\?\$?\w+)\s+\|\s?(.+)?", line)

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
    
    if currentInput.startswith("\\$") or currentStack.startswith("\\$") or nextState.startswith("\\$"):
        closure.append((currentState, currentInput, currentStack, nextState, nextStack))
        continue
    rule.append((nextState, nextStack))

pda = PDA(statePDA, inputPDA, stackPDA, startState, startStack, transition)

pda.start("""
<html>
<head> 
  <title>Simple Webpage</title>

</head>
<body>

<h2>HTML Forms</h2>

<form action="/action_page.php" method="post">
  <h5 class="label">First name:</h5><br>
  <input type="text" id="fname"><br>
  <h5 class="label">Last name:</h5><br>
  <input type="text" id="lname"><br><br>
  <button type="submit">Submit</button>
</form> 

<p>If you click the "Submit" button, the form-data will be sent to a page called "/action_page.php".</p>

</body>
</html>

""")