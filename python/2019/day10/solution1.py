input = [line.strip() for line in open("input.txt").readlines()]

mapSize = len(input) - 1

spaceMap = [[char == "#" for char in line] for line in input]

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


def countVisible(asteroidLocations, x, y):
    global currentPosition

    blockedLocations = []
    visibleCount = 0
    currentPosition = [x, y]

    asteroidLocations.sort(key=calcDistance) #sort by nearest

    for asteroidLocation in asteroidLocations:
        if asteroidLocation not in blockedLocations and not (asteroidLocation[0] == x and asteroidLocation[1] == y): #if the asteroid is visible and isnt the same as the current one
            visibleCount += 1

            #block all the invisible asteroids
            tilt = getTilt(currentPosition[0], currentPosition[1], asteroidLocation[0], asteroidLocation[1])
            if type(tilt) == float or type(tilt) == int:
                points = getPoints(asteroidLocation, -1 if currentPosition[0] > asteroidLocation[0] else 1, tilt)
            else:
                points = getVerticalLinePositions(asteroidLocation, -1 if currentPosition[1] > asteroidLocation[1] else 1)
            for blockedLocaton in points:
                if blockedLocaton in asteroidLocations:
                    blockedLocations.append(blockedLocaton)

        """ print(f"{asteroidLocation}:{blockedLocations}") """
    
    print(blockedLocations)

    return len(asteroidLocations) - len(blockedLocations) - 1
    """ for asteroidLocation in asteroidLocations:
        if asteroidLocation not in blockedLocations:
            print(asteroidLocation) """

""" print(getTilt(4, 2, 3, 2))

print(getPoints([3,2],-1,0)) """

maxAsteroids = 0
maxPosition = [0,0]

for asteroidLocation in asteroidLocations:
    visible = countVisible(asteroidLocations, asteroidLocation[0], asteroidLocation[1])
    if visible > maxAsteroids:
        maxAsteroids = visible
        maxPosition[0] = asteroidLocation[0]
        maxPosition[1] = asteroidLocation[1]

print(maxAsteroids)
print(maxPosition)

""" print(countVisible(asteroidLocations, 11, 13)) """

""" print(asteroidLocations) """

#print(countVisible(asteroidLocations, 0, 1))

#print(getPoints([0,1], 1, getTilt(0,1,3,3)))

#print(getTilt(0,1,3,3))

#6,3
#9,7