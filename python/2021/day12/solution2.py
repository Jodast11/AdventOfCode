def discoverPaths(mapOfCaves, smallCavesVisitedOrig, currentLocation, hasVisitedDouble):
    newPaths = []
    smallCavesVisited = smallCavesVisitedOrig.copy()
    if not currentLocation.isupper():
        smallCavesVisited.append(currentLocation)
    for path in mapOfCaves[currentLocation]:
        if path == "end":
            newPaths.append(","+path)
        elif path not in smallCavesVisited:
            for newPath in discoverPaths(mapOfCaves,smallCavesVisited,path, hasVisitedDouble):
                newPaths.append(","+path+newPath)
        elif path in smallCavesVisited and not hasVisitedDouble and path != "start" and path != "end":
            for newPath in discoverPaths(mapOfCaves,smallCavesVisited,path, True):
                newPaths.append(","+path+newPath)

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
    

# print(mapOfCaves)

allNewPaths = []

for newPath in discoverPaths(mapOfCaves,[],"start",False):
    allNewPaths.append("start" + newPath)
    # print(allNewPaths[-1])

print(len(allNewPaths))