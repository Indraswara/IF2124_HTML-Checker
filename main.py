
# Production Rule
# Dictionary<StringVariable, List<StringRule>>
productionRule: dict[str, list[str]] = {
    "P": ["0", "1", "0P0", "1P1"]
}


# Instantenous Description
# Tuple<StringState, StringStack, StringInput>
ID = tuple[str, str, str]

# Job
# Queue of ID
job: list[ID] = []

def isJobEmpty():
    return len(job) == 0

startID: ID = ("p", "P", "10101")


def main():
    job.append(startID)

    verdict: bool = False

    while len(job) != 0:
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
                job.append((state, production + restStack, topInput + restInput))

    if verdict:
        print("Accepted")
    else:
        print("Not Accepted")

main()