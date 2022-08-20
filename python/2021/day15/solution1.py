import string

class waypoint:
    def __init__(self, name, distanceToStart) -> None:
        self.name = name
        self.distanceToStart = distanceToStart
        self.previous = None

    def setPrevious(self,value):
        self.previous = value

    def setDistance(self,value):
        self.distanceToStart = value

def printWaypoints(waypointsToPrint):
    keys = list(waypointsToPrint.keys())
    for key in keys:
        print(str(waypointsToPrint[key].name)+":"+str(waypointsToPrint[key].previous)+" "+str(waypointsToPrint[key].distanceToStart))

def sortWaypoints(waypointsToSort):
    newList = sorted((value.distanceToStart, key) for (key, value) in waypointsToSort.items())
    newDict = dict([(k,waypointsToSort[k]) for v,k in newList])
    return newDict

def findNeighbours(waypoints, currentWaypoint):
    neighboursFound = []
    waypointKeys = list(waypoints.keys())
    if (currentWaypoint.name[0]+1,currentWaypoint.name[1]) in waypointKeys:
        neighboursFound.append((currentWaypoint.name[0]+1,currentWaypoint.name[1]))
    if (currentWaypoint.name[0]-1,currentWaypoint.name[1]) in waypointKeys:
        neighboursFound.append((currentWaypoint.name[0]-1,currentWaypoint.name[1]))
    if (currentWaypoint.name[0],currentWaypoint.name[1]+1) in waypointKeys:
        neighboursFound.append((currentWaypoint.name[0],currentWaypoint.name[1]+1))
    if (currentWaypoint.name[0],currentWaypoint.name[1]-1) in waypointKeys:
        neighboursFound.append((currentWaypoint.name[0],currentWaypoint.name[1]-1))
    return neighboursFound

infinitie = 999999999999999999

field = [[int(field) for field in line.strip()] for line in open("input.txt").readlines()]

allUnfinishedWaypoints = {}
finishedWaypoints = {}

for y, line in enumerate(field):
    for x, value in enumerate(line):
        allUnfinishedWaypoints[(x,y)] = waypoint((x,y), infinitie)

allUnfinishedWaypoints[(0,0)] = waypoint((0,0),0)

foundPathToEnd = False

while len(allUnfinishedWaypoints) != 0:

    allUnfinishedWaypoints = sortWaypoints(allUnfinishedWaypoints)

    # printWaypoints(allUnfinishedWaypoints)

    currentWaypoint = allUnfinishedWaypoints[list(allUnfinishedWaypoints.keys())[0]]

    for neighbourName in findNeighbours(allUnfinishedWaypoints,currentWaypoint):
        if allUnfinishedWaypoints[neighbourName].distanceToStart > currentWaypoint.distanceToStart + field[neighbourName[0]][neighbourName[1]]:
            allUnfinishedWaypoints[neighbourName].distanceToStart = currentWaypoint.distanceToStart + field[neighbourName[0]][neighbourName[1]]
            allUnfinishedWaypoints[neighbourName].previous = currentWaypoint.name
        if neighbourName == (99,99):
            foundPathToEnd = True

    # print()

    finishedWaypoints[currentWaypoint.name] = allUnfinishedWaypoints.pop(currentWaypoint.name)

    # allUnfinishedWaypoints = sortWaypoints(allUnfinishedWaypoints)

    # printWaypoints(allUnfinishedWaypoints)



# printWaypoints(sortWaypoints(finishedWaypoints))
print(finishedWaypoints[(99,99)].distanceToStart)
