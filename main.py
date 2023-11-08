variables: list[str] = ["S","A"]

# Production Rule
# Dictionary<StringVariable, List<StringRule>>
productionRule: dict[str, list[list[str]]] = {
    "S": ["0S", "A"],
    "A": ["1A", "1"],
}

# Instantenous Description
# Tuple<StringState, StringStack, StringInput>
ID = tuple[str, str, str]

# Job
# Queue of ID
job: list[ID] = []

startID: ID = ("p", "S", "0011")

def countTerminal(string: str) -> int:
    count = 0
    for c in string:
        if not c in variables:
            count += 1
    return count

def main():
    job.append(startID)

    verdict: bool = False

    while len(job) != 0:
        (state, stack, input) = job.pop(0)
        # print(state, stack, "\t", input)

        if len(stack) == 0 or len(input) == 0:
            if len(stack) == 0 and len(input) == 0:
                verdict = True
                break
            continue

        if countTerminal(stack) > len(input):
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