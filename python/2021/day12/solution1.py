def discoverPaths(mapOfCaves, smallCavesVisitedOrig, currentLocation):
    newPaths = []
    smallCavesVisited = smallCavesVisitedOrig.copy()
    if not currentLocation.isupper():
        smallCavesVisited.append(currentLocation)
    for path in mapOfCaves[currentLocation]:
        if path == "end":
            newPaths.append(path)
        elif path not in smallCavesVisited:
            for newPath in discoverPaths(mapOfCaves,smallCavesVisited,path):
                newPaths.append(path+newPath)
    return newPaths

inputRaw = [line.strip() for line in open("input.txt")]

mapOfCaves = {}
paths = []

for connection in inputRaw:
    parts = connection.split("-")
    for i in range(2):
        if parts[i] not in mapOfCaves:
            mapOfCaves[parts[i]] = [parts[not i]]
        else:
            mapOfCaves[parts[i]] += [parts[not i]]

print(len(discoverPaths(mapOfCaves,[],"start")))