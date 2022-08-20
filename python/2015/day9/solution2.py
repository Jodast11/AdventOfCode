#floodfill? kreisartig? ameisen? bruteforce!

def getShortestRoute(routes, locationsVisited, length, currentLocation):
    if len(locationsVisited) == len(routes): #if every location has been visited
        return length
    
    nextPathLengths = []
    for destination in routes[currentLocation]:
        if destination[0] not in locationsVisited:
            nextPathLengths.append(getShortestRoute(routes, locationsVisited + [destination[0]], length+destination[1], destination[0]))
    return max(nextPathLengths)

lines = [x.strip() for x in open("input.txt")]

routes = {}

for route in lines:
    source = route.split(" to ")[0]
    destination = route.split(" to ")[1].split(" = ")[0]
    length = int(route.split(" = ")[1])

    if source not in routes:
        routes[source] = [(destination, length)]
    else:
        routes[source].append((destination, length))

    if destination not in routes:
        routes[destination] = [(source, length)]
    else:
        routes[destination].append((source, length))


pathLengths = []
for startLocation in routes:
    pathLengths.append(getShortestRoute(routes, [startLocation], 0, startLocation))

print(max(pathLengths))