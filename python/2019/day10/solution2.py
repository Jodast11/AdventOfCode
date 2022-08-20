import math

puzzleInput = [line.strip() for line in open("input.txt").readlines()]

mapSize = len(puzzleInput[0]) - 1

spaceMap = [[char == "#" for char in line] for line in puzzleInput]

asteroidLocations = []

currentPosition = [0,0]

for y, line in enumerate(spaceMap):
    for x, containsAsteroid in enumerate(line):
        if containsAsteroid:
            asteroidLocations.append([x,y])

def getPoints(startPosition, direction, tilt):
    global mapSize
    points = []
    currentPosition = [startPosition[0], startPosition[1]]
    while currentPosition[0] <= mapSize and currentPosition[0] >= 0 and currentPosition[1] <= mapSize and currentPosition[1] >= 0:
        if float(round(currentPosition[1], 9)).is_integer() and currentPosition != startPosition:
            points.append([int(currentPosition[0]), int(round(currentPosition[1], 9))])
        currentPosition[0] += direction
        currentPosition[1] += tilt * direction
        currentPosition[0] = currentPosition[0]
        currentPosition[1] = currentPosition[1]
    return points

def getTilt(x1, y1, x2, y2):
    dy = (y2 - y1)
    dx = (x2-x1)
    if dx != 0:
        return dy/dx

def calcDistance(asteroidPosition):
    global currentPosition
    return abs(asteroidPosition[0]-currentPosition[0]) + abs(asteroidPosition[1]-currentPosition[1])

def getVerticalLinePositions(startPosition, direction):
    points = []
    currentPosition = [startPosition[0], startPosition[1]]
    while currentPosition[1] <= mapSize and currentPosition[1] >= 0:
        currentPosition[1] += direction
        newPoint = [currentPosition[0], currentPosition[1]]
        if newPoint != startPosition:
            points.append(newPoint)
    return points

def getVisible(asteroidLocations, x, y):
    global currentPosition

    blockedLocations = []
    currentPosition = [x, y]

    asteroidLocations.sort(key=calcDistance) #sort by nearest

    for asteroidLocation in asteroidLocations:
        if asteroidLocation not in blockedLocations and not (asteroidLocation[0] == x and asteroidLocation[1] == y): #if the asteroid is visible and isnt the same as the current one

            #block all the invisible asteroids
            tilt = getTilt(currentPosition[0], currentPosition[1], asteroidLocation[0], asteroidLocation[1])
            if type(tilt) == float or type(tilt) == int:
                points = getPoints(asteroidLocation, -1 if currentPosition[0] > asteroidLocation[0] else 1, tilt)
            else:
                points = getVerticalLinePositions(asteroidLocation, -1 if currentPosition[1] > asteroidLocation[1] else 1)
            for blockedLocaton in points:
                if blockedLocaton in asteroidLocations:
                    blockedLocations.append(blockedLocaton)
    
    visibleAsteroids = []

    for asteroidLocation in asteroidLocations:
        if asteroidLocation not in blockedLocations:
            visibleAsteroids.append(asteroidLocation)

    return visibleAsteroids

def getAngle(p):
    global center
    dx = center[0]-p[0]
    dy = center[1]-p[1]
    if dx:
        return abs(math.degrees(math.atan(dy/dx)))
    else:
        return 90

def splitCircle(visible):
    global center
    quarters = [[],[],[],[]]

    cx = center[0]
    cy = center[1]

    for point in visible:
        px = point[0]
        py = point[1]

        if px >= cx and py < cy:
            quarters[0].append(point)
            continue
        
        if px > cx and py >= cy:
            quarters[1].append(point)
            continue

        if px <= cx and py > cy:
            quarters[2].append(point)
            continue

        if px < cx and py <= cy:
            quarters[2].append(point)
            continue

    quarters[0].sort(key=getAngle)
    quarters[1].sort(key=getAngle)
    quarters[2].sort(key=getAngle)
    quarters[3].sort(key=getAngle)

    quarters[0] = quarters[0][::-1]
    quarters[1] = quarters[1][::-1]
    quarters[2] = quarters[2][::-1]
    quarters[3] = quarters[3][::-1]

    return quarters[0] + quarters[1] + quarters[2] + quarters[3]

#get visible
#cast to four lines (one per quarter)
#get sequence

center = [11, 13]

visible = getVisible(asteroidLocations, 11, 13)

quarters = splitCircle(visible)

while True:
    print(quarters[int(input(">"))])

""" for v in visible:
    print(f"{math.degrees(getAngle(v))}:{v}") """