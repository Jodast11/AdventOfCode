def getOverlapping(xStart1, xEnd1, yStart1, yEnd1, zStart1, zEnd1, xStart2, xEnd2, yStart2, yEnd2, zStart2, zEnd2):
    xOverlapStart = xStart1 if xStart1 > xStart2 else xStart2
    xOverlapEnd = xEnd1 if xEnd1 < xEnd2 else xEnd2

    if xOverlapStart > xOverlapEnd:
        return False
    
    yOverlapStart = yStart1 if yStart1 > yStart2 else yStart2
    yOverlapEnd = yEnd1 if yEnd1 < yEnd2 else yEnd2

    if yOverlapStart > yOverlapEnd:
        return False

    zOverlapStart = zStart1 if zStart1 > zStart2 else zStart2
    zOverlapEnd = zEnd1 if zEnd1 < zEnd2 else zEnd2

    if zOverlapStart > zOverlapEnd:
        return False

    return True

input = [line.strip() for line in open("input.txt").readlines()]

allCoordinates = []

for opperation in input:
    coordinates = [(int(coordinateRaw.split("..")[0][2:]), int(coordinateRaw.split("..")[1])) for coordinateRaw in opperation.split(" ")[1].split(",")]
    allCoordinates.append(coordinates)

switchedOn = 0

for index, coordinateSet1 in enumerate(allCoordinates):
    isOverlapping = False
    for coordinateSet2 in allCoordinates:
        if coordinateSet2 != coordinateSet1:
            if getOverlapping(coordinateSet1[0][0],coordinateSet1[0][1],coordinateSet1[1][0],coordinateSet1[1][1],coordinateSet1[2][0],coordinateSet1[2][1],coordinateSet2[0][0],coordinateSet2[0][1],coordinateSet2[1][0],coordinateSet2[1][1],coordinateSet2[2][0],coordinateSet2[2][1]):
                isOverlapping = True
                break
    if "on" in input[index]:
        switchedOn += (coordinateSet1[0][1]-coordinateSet1[0][0]) * (coordinateSet1[1][1]-coordinateSet1[1][0]) * (coordinateSet1[2][1]-coordinateSet1[2][0])

print(switchedOn)
