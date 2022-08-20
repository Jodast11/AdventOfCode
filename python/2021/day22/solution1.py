def getCubes(xStart, xEnd, yStart, yEnd, zStart, zEnd):
    cubes = []

    if xEnd < -50:
        return []
    if yEnd < -50:
        return []
    if zEnd < -50:
        return []

    if xStart > 50:
        return []
    if yStart > 50:
        return []
    if zStart > 50:
        return []

    if xStart < -50:
        xStart = -50
    if yStart < -50:
        yStart = -50
    if zStart < -50:
        zStart = -50
    
    if xEnd > 50:
        xEnd = 50
    if yEnd > 50:
        yEnd = 50
    if zEnd > 50:
        zEnd = 50

    for x in range(xStart,xEnd+1):
        for y in range(yStart,yEnd+1):
            for z in range(zStart,zEnd+1):
                if x+50 >= 0 and y+50 >= 0 and z+50 >= 0 and x+50 < 101 and y+50 < 101 and z+50 < 101:
                    cubes.append((x+50,y+50,z+50))  
    return cubes

def doOpperation(opperation, reactor):
    if "on" in opperation:
        newState = True
    else:
        newState = False
    
    coordinates = [(int(coordinateRaw.split("..")[0][2:]), int(coordinateRaw.split("..")[1])) for coordinateRaw in opperation.split(" ")[1].split(",")]

    for cubeToChange in getCubes(coordinates[0][0],coordinates[0][1],coordinates[1][0],coordinates[1][1],coordinates[2][0],coordinates[2][1]):
        # print(cubeToChange[0],cubeToChange[1],cubeToChange[2])
        reactor[cubeToChange[0]][cubeToChange[1]][cubeToChange[2]] = newState

    return reactor



input = [line.strip() for line in open("input.txt").readlines()]

# getCubes(10,12,10,12,10,12)

reactor = [[[False for i in range(101)] for j in range(101)] for k in range(101)]

# reactor[0][0][0] = True

# doOpperation("on x=10..12,y=10..12,z=10..12", reactor)

for i, line in enumerate(input):
    reactor = doOpperation(line, reactor)
    print(i)

print(str(reactor).count("True"))

