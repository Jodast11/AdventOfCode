def getRelativePosition(posA, posB):
    return (posB[0]-posA[0], posB[1]-posA[1])

def tupleAbs(pos):
    return (abs(pos[0]), abs(pos[1]))

def simplify(pos):
    for i in range(max(tupleAbs(pos)), 1, -1):
        if pos[1] % i == 0 and pos[0] % i == 0:
            return (int(pos[0]/i), int(pos[1]/i))
    return pos

input = [line.strip() for line in open("input.txt").readlines()]

asteroidPositions = []

for y, line in enumerate(input):
    for x, isAsteroid in enumerate(line):
        if isAsteroid == "#":
            asteroidPositions.append((x,y))

asteroidPositions.sort()

print(max([len(list(set([simplify(getRelativePosition(possibleStationPos, asteroidPosition)) for asteroidPosition in asteroidPositions])))-1 for possibleStationPos in asteroidPositions]))