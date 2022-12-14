programm = open("input.txt").read().split("\n")
solution = 0

def checkIfRelevant(currentCycle, x):
    global solution
    if not currentCycle % 20 and currentCycle % 40:
       solution += currentCycle*x

x = 1
currentCycle = 0

for instruction in programm:
    currentCycle += 1
    checkIfRelevant(currentCycle, x)
    if "a" in instruction:
        currentCycle += 1
        checkIfRelevant(currentCycle, x)
        x += int(instruction.split(" ")[-1])

print(solution)