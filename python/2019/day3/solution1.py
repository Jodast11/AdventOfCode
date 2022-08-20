circuitBoard = {}

def savePosition(position, cableID):
    global circuitBoard
    if position in circuitBoard.keys():
        circuitBoard[position].append(cableID)
    else:
        circuitBoard[position] = [cableID]

def getPath(cable, cableID):
    directions = {"U":[0,1],"D":[0,-1],"L":[-1,0],"R":[1,0]}
    posX = 0
    posY = 0

    for instruction in cable:
        direction = instruction[0]
        length = int(instruction[1:])
        for i in range(length):
            posX += directions[direction][0]
            posY += directions[direction][1]
            position = str(posX)+":"+str(posY)
            savePosition(position, cableID)

def getOverlapping():
    global circuitBoard
    overlapping = []
    for position in circuitBoard.keys():
        cables = list(dict.fromkeys(circuitBoard[position]))
        if len(cables) > 1:
            overlapping.append(position)
    return overlapping
                

input = [line.strip() for line in open("input.txt").readlines()]

getPath(input[0].split(","), 69)
getPath(input[1].split(","), 420)

print(min([abs(int(position.split(":")[0]))+abs(int(position.split(":")[1])) for position in getOverlapping()]))