import json
import re
from loader import loaderCNF
from cnf import *

cnf = loaderCNF

variables: list[str] = cnf.variables

# Production Rule
# Dictionary<StringVariable, List<StringRule>>
productionRule: dict[str, list[list[str]]] = cnf.productionRules

# Instantenous Description
# Tuple<StringState, StringStack, StringInput>
ID = tuple[str, list[str], list[str]]

# Job
# Queue of ID
job: list[ID] = []

startID: ID = ("p", [cnf.startVariables], list("A -> a | aAa | aaaa | aaA \n                                    A -> a"))

wait = input

def formatID(id: ID):
    (_, stack, input) = id
    return '|'.join(stack) + "\t\t" + ''.join(input)

def main():
    job.append(startID)

    verdict: bool = False

    counter = 0
    while len(job) != 0:
        counter += 1
        print(counter)

        # prompt = wait()
        # if prompt == "":
        #     f = open("demofile2.txt", "w")
        #     output = list(map(formatID, job))
        #     f.write("\n".join(output))
        #     f.close()

        (state, stack, input) = job.pop(0)

        if len(stack) == 0 or len(input) == 0:
            if len(stack) == 0 and len(input) == 0:
                verdict = True
                break
            continue

        topStack = stack[0]
        restStack = stack[1:]
        topInput = input[0]
        restInput = input[1:]

        currentProductionRule = productionRule.get(topStack)
        if currentProductionRule == None:
            if topStack == topInput:
                job.append((state, restStack, restInput))
        else:
            for production in currentProductionRule:
                job.append((state, production + restStack, [topInput] + restInput))

    if verdict:
        return 1
    else:
        return 0
