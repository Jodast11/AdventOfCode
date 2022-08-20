def getRotationResults(positions):
    results = []
    
    rotationOpperators = [
        [(0,0),(0,1),(0,2)],
        [(0,0),(1,2),(0,1)],
        [(0,0),(1,1),(1,2)],
        [(0,0),(0,2),(1,1)],
        [(1,0),(1,1),(0,2)],
        [(1,0),(1,2),(1,1)],
        [(1,0),(0,1),(1,2)],
        [(1,0),(0,2),(0,1)],
        [(0,1),(0,0),(1,2)],
        [(0,1),(1,0),(0,2)],
        [(0,1),(0,2),(0,0)],
        [(0,1),(1,2),(1,0)],
        [(1,1),(0,0),(0,2)],
        [(1,1),(1,0),(1,2)],
        [(1,1),(1,2),(0,0)],
        [(1,1),(0,2),(1,0)],
        [(0,2),(0,0),(0,1)],
        [(0,2),(1,0),(1,1)],
        [(0,2),(1,1),(0,0)],
        [(0,2),(0,1),(1,0)],
        [(1,2),(0,0),(1,1)],
        [(1,2),(1,0),(0,1)],
        [(1,2),(0,1),(0,0)],
        [(1,2),(1,1),(1,0)]
    ]

    for operationStep in rotationOpperators:
            newCoords = []
            for position in positions:
                newCoords.append([position[operationStep[0][1]] * (-1 if operationStep[0][0] else 1), position[operationStep[1][1]] * (-1 if operationStep[1][0] else 1), position[operationStep[2][1]] * (-1 if operationStep[2][0] else 1)])
            results.append(newCoords)

    return results

inputsRaw = [open("input.txt","r").read().split("\n\n")][0]

scanResults = []

for inputRaw in inputsRaw:
    scanResult = []
    for line in inputRaw.split("\n")[1:]:
        scanResult.append([int(x) for x in line.split(",")])
    scanResults.append(scanResult)

