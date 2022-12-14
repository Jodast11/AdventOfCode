import os

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    instructions = [x for x in f.read().split("\n")[0]]

def getVisitedHouses(instructions):
    xPos = 0
    yPos = 0

    visitedHouses = [(xPos,yPos)]

    for instruction in instructions:
        if instruction == "^":
            yPos += 1
        if instruction == "v":
            yPos -= 1
        if instruction == ">":
            xPos += 1
        if instruction == "<":
            xPos -= 1

        visitedHouses.append((xPos,yPos))

    return list(dict.fromkeys(visitedHouses))

instructionsSanta = ""
instructionsRobot = ""

santaInstruction = True
for instruction in instructions:
    if santaInstruction:
        instructionsSanta += instruction
    else:
        instructionsRobot += instruction
    santaInstruction = not santaInstruction

santaVisited = getVisitedHouses(instructionsSanta)
robotVisited = getVisitedHouses(instructionsRobot)

for location in robotVisited:
    santaVisited.append(location)

print(len(list(dict.fromkeys(santaVisited))))