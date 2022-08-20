import time

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

fieldOriginal = [[int(field) for field in line.strip()] for line in open("input.txt").readlines()]

field = []
for line in fieldOriginal:
    newLine = []
    for offset in range(5):
        for value in line: 
            if value + offset < 10:
                newLine.append(value + offset)
            else:
               newLine.append(value + offset - 9) 
    field.append(newLine)

fieldOriginal = field.copy()

field = []

for offset in range(5):
    for line in fieldOriginal:
        newLine = []
        for value in line:
            if value + offset < 10:
                newLine.append(value + offset)
            else:
                newLine.append(value + offset - 9) 
        field.append(newLine)


            
# print(field)

allUnfinishedWaypoints = {}
finishedWaypoints = {}

for y, line in enumerate(field):
    for x, value in enumerate(line):
        allUnfinishedWaypoints[(x,y)] = waypoint((x,y), infinitie)

allUnfinishedWaypoints[(0,0)] = waypoint((0,0),0)

waypointsDistanceCalculated = [allUnfinishedWaypoints[(0,0)]]

done = False

while not done:
    print(len(allUnfinishedWaypoints))
    values = [content.distanceToStart for content in allUnfinishedWaypoints.values()]
    currentWaypointName = list(allUnfinishedWaypoints.keys())[values.index(min(values))]
    currentWaypoint = allUnfinishedWaypoints[currentWaypointName]
    for neighbourName in findNeighbours(allUnfinishedWaypoints,currentWaypoint):
        if allUnfinishedWaypoints[neighbourName].distanceToStart > currentWaypoint.distanceToStart + field[neighbourName[0]][neighbourName[1]]:
            allUnfinishedWaypoints[neighbourName].distanceToStart = currentWaypoint.distanceToStart + field[neighbourName[0]][neighbourName[1]]
        if neighbourName == (len(field)-1,len(field)-1):
            done = True
    finishedWaypoints[currentWaypointName] = allUnfinishedWaypoints.pop(currentWaypointName)



print(allUnfinishedWaypoints[(len(field)-1,len(field)-1)].distanceToStart)