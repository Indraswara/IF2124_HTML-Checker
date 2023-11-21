from PDA import Transition
rawConfig = open("pda.config", "r").read()
lines = rawConfig.split("\n")

statePDA = lines.pop(0)
inputPDA = lines.pop(0)
stackPDA = lines.pop(0)

transition: Transition = {}