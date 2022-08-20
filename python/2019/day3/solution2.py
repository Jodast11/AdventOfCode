circuitBoard = {} #[cableID, steps]
intersections = {}

def savePosition(position, cableID, steps):
    global circuitBoard
    if position in circuitBoard.keys():
        if circuitBoard[position][0] != cableID:
            if position not in intersections:
                intersections[position] = steps + circuitBoard[position][1]
        circuitBoard[position].append(cableID)
    else:
        circuitBoard[position] = [cableID, steps]

def getPath(cable, cableID):
    directions = {"U":[0,1],"D":[0,-1],"L":[-1,0],"R":[1,0]}
    posX = 0
    posY = 0
    steps = 0

    for instruction in cable:
        direction = instruction[0]
        length = int(instruction[1:])
        for i in range(length):
            steps += 1
            posX += directions[direction][0]
            posY += directions[direction][1]
            position = str(posX)+":"+str(posY)
            savePosition(position, cableID, steps)

input = [line.strip() for line in open("input.txt").readlines()]

getPath(input[0].split(","), 69)
getPath(input[1].split(","), 420)

print(min([intersections[intersection] for intersection in intersections.keys()]))