import math

def getRelativePosition(posA, posB): #Returns the relative distance between two points
    return (posB[0]-posA[0], posB[1]-posA[1])

def tupleAbs(pos): #Makes a tuple positive
    return (abs(pos[0]), abs(pos[1]))

def simplify(pos): #Gets the simplest representation of vector ([4,12] -> [1,3])
    for i in range(max(tupleAbs(pos)), 1, -1):
        if pos[1] % i == 0 and pos[0] % i == 0:
            return (int(pos[0]/i), int(pos[1]/i))
    return pos

def vectorAngle(vecA, vecB): #Calculates the angle between two vectors
    a, b = vecA
    c, d = vecB
    dotProduct = a*c + b*d
    modOfVector1 = math.sqrt( a*a + b*b)*math.sqrt(c*c + d*d) 
    angle = dotProduct/modOfVector1
    return math.degrees(math.acos(angle))

def calcAngleA(vec): #Used to sort vector that point to the left
    return vectorAngle((0, -1), vec)

def calcAngleB(vec): #Used to sort vector that point to the right
    return vectorAngle((0, 1), vec)

def getStationOffset(pos):
    global stationPosition
    return abs(pos[0]-stationPosition[0])+abs(pos[1]-stationPosition[1])

input = [line.strip() for line in open("input.txt").readlines()]

asteroidPositions = [] #All the positions were asteroids are

for y, line in enumerate(input): #Retrieve the positions of the asteroids
    for x, isAsteroid in enumerate(line):
        if isAsteroid == "#":
            asteroidPositions.append((x,y))

asteroidPositions.sort() #Srt for convenience

#We need to first get the place withe the most visible asteroids, that are not blocked by others

stationPosition = (0,0)
maxAsteroids = 0

for possibleStationPos in asteroidPositions:
    asteroidCount = len(list(set([simplify(getRelativePosition(possibleStationPos, asteroidPosition)) for asteroidPosition in asteroidPositions])))-1 #We get the amont of unique simplified vectors to all the other points
    if asteroidCount > maxAsteroids:
        maxAsteroids = asteroidCount
        stationPosition = possibleStationPos

#Now we know from wich asteroid we can view the most others. We will now have to sort the vectors, so they are in the correct order (clockwise, from position up)

#stationPosition = (11, 13)

asteroidDirections = {}

for asteroidPosition in asteroidPositions:
    if asteroidPosition != stationPosition:
        direction = simplify(getRelativePosition(stationPosition, asteroidPosition))
        if direction not in asteroidDirections:
            asteroidDirections[direction] = [asteroidPosition]
        else:
            asteroidDirections[direction].append(asteroidPosition)

directions = list(asteroidDirections.keys())

directionGroups = [[], []]

for direction in directions:
    if direction[0] >= 0:
        directionGroups[0].append(direction)
    else:
        directionGroups[1].append(direction)

directionGroups[0].sort(key=calcAngleA)

directionGroups[1].sort(key=calcAngleB)

directions = directionGroups[0] + directionGroups[1]

asteroidsDestroied = 0
currentAngleIndex = 0

for destroyTarget in directions:
    asteroidDirections[destroyTarget].sort(key=getStationOffset)

while True:
    if len(asteroidDirections[directions[currentAngleIndex]]) != 0:
        destroidAsteroid = asteroidDirections[directions[currentAngleIndex]].pop(0)
        asteroidsDestroied += 1
        if asteroidsDestroied > 199:
            print(destroidAsteroid[0]*100+destroidAsteroid[1])
            break
    currentAngleIndex += 1
    currentAngleIndex %= len(directions)
