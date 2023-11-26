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
    
    if currentInput.startswith("\\$") or currentStack.startswith("\\$") or nextState.startswith("\\$"):
        closure.append((currentState, currentInput, currentStack, nextState, nextStack))
        continue
    rule.append((nextState, nextStack))

pda = PDA(statePDA, inputPDA, stackPDA, startState, startStack, transition)
pda.start("""
<   html > 
    <head>
    <script> ini random () banget tcuy #$%^ </script>
    <tiTlE> ini title random tcuy </titLe>
    </HeAd> 
    <BodY> 
        <H1 class = "ini Checker yang kami buat"      
          > ini judul H1 # </h1>
        <p> masukkan inputmu disini atau Rating Kami</P>
        <input type = "password" id = "harus" class = "harus kamu isi kalo gak aku hantuin!!!!!!" />
        <form method = "GET" class = "ini adalah method"> </form>
        < p id = "momen()"><em> ini momen bjir</Em> </P>
        <p id = "$%^&*#@"> <strong id = "@#$%^&"> Ini #$%</strong> </P>
          <div id = "momen"> 
            <Div id = "showoff">
                <dIv id = "brutal">
                    <dIv id = "psikopat">
                        <DiV id = "Manayangnulis"       
                            >
                            <DIv id = "HTML">
                                <div class = "Begini BJIR BJIR BJIR BJIR bjir">
                                    <p>
                                        <Em> this is FORMATED TEXT</eM>
                                    </P>
                                </div>
                                <diV>
                                <DIV> 
                                    <p> Ini stress tress kami paling brutal silakan dicoba </P>

                                    <H5 id = "Yakinkamumas"> Cepet mas kerJain!!!! < /h5>
                                </dIV>
                                    <p> </P>
                                    <tabLe>
                                        <tr>
                                        <td>
                                            <b><ABBR> Ini SH 0W 0Ff!!!!!!%$#^&*@ </AbbR></B>
                                        </td>
                                        </tr>
                                        <th>
                                        <td>
                                        </td>
                                        </th>
                                    </TaBlE>
                                </DIv>
                            </DIv>
                        </DIv>
                    </div>
                </diV>
            </diV>
          </diV>
    </BOdY>
< /html    >
""")