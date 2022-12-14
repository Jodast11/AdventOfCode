lines = [x.strip() for x in open("input.txt")][0].split(", ")

def rotate(direction, currentrotation):
    if direction == "L":
        newrotation = currentrotation - 1
        if newrotation < 0:
            newrotation = 3
        return newrotation
    else:
        newrotation = currentrotation + 1
        if newrotation > 3:
            newrotation = 0
        return newrotation

def getPosVisited(horStart, verStart, horEnd, verEnd):
    visitedPositions = []
    if horStart == horEnd:
        for v in range(verStart+1,verEnd+1, -1 if verStart>verEnd else 1):
            visitedPositions.append(str(horStart)+"|"+str(v))
    else:
        for h in range(horStart+1,horEnd+1, -1 if horStart>horEnd else 1):
            visitedPositions.append(str(h)+"|"+str(verStart))
    return visitedPositions

rotation = 0

posHor = 0
posVer = 0

posVisited = ["0|0"]

for line in lines:
    horStart = posHor
    verStart = posVer
    rotation = rotate(line[0], rotation)
    if rotation == 0:
        posHor += int(line[1:])
    if rotation == 2:
        posHor -= int(line[1:])
    if rotation == 1:
        posVer += int(line[1:])
    if rotation == 3:
        posVer -= int(line[1:])
    
    for newLoc in getPosVisited(horStart, verStart, posHor, posVer):
        if newLoc in posVisited:
            print(abs(posHor)+abs(posVer))
            exit()
        posVisited.append(newLoc)
    print(posVisited)