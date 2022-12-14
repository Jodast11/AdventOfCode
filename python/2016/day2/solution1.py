def calculateNumber(cords):
    return (cords[1]*3)+cords[0]+1

instructionLines = [x.strip() for x in open("input.txt")]

currentCords = [1,1]

for instructionLine in instructionLines:
    for instruction in instructionLine:
        if instruction == "U":
            if currentCords[1] - 1 >= 0 and currentCords[1] - 1 <= 2:
                currentCords[1] -= 1
        if instruction == "D":
            if currentCords[1] + 1 >= 0 and currentCords[1] + 1 <= 2:
                currentCords[1] += 1
        if instruction == "R":
            if currentCords[0] + 1 >= 0 and currentCords[0] + 1 <= 2:
                currentCords[0] += 1
        if instruction == "L":
            if currentCords[0] - 1 >= 0 and currentCords[0] - 1 <= 2:
                currentCords[0] -= 1
    print(calculateNumber(currentCords), end="")

print()

