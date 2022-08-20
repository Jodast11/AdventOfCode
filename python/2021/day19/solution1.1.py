import time

class Scanner:
    def __init__(self, id, beakonLocations):
        self.id = id
        self.beakonLocations = beakonLocations
        self.overlappingScannerId = -1
        self.facingDirection = 0 #0:up 1:down 2:left 3:right 4:back 5:forth
        self.rotation = 0
        self.currentVariation = [(beakonLocation[0], beakonLocation[1], beakonLocation[2]) for beakonLocation in beakonLocations]
        self.offset = None

    def rotate(self):
        self.rotation += 1
        self.rotation %= 4
        self.currentVariation = [(-beakonLocation[1], beakonLocation[0], beakonLocation[2]) for beakonLocation in self.currentVariation]

    def turn(self):
        turningOperations = [((1,0),(1,1),(1,2)), ((-1,0),(1,1),(-1,2)), ((-1,2),(1,1),(1,0)), ((1,2),(1,1),(-1,0)), ((1,0),(-1,2),(1,1)), ((1,0),(1,2),(-1,1))] #starting from looking up
        turningBackOperations = [((1,0),(1,1),(1,2)), ((-1,0),(1,1),(-1,2)), ((1,2),(1,1),(-1,0)), ((-1,2),(1,1),(1,0)), ((1,0),(1,2),(-1,1)), ((1,0),(-1,2),(1,1))]


        #first turn back to the upwards position
        self.currentVariation = [(beakonLocation[turningBackOperations[self.facingDirection][0][1]] * turningBackOperations[self.facingDirection][0][0], beakonLocation[turningBackOperations[self.facingDirection][1][1]] * turningBackOperations[self.facingDirection][1][0], beakonLocation[turningBackOperations[self.facingDirection][2][1]] * turningBackOperations[self.facingDirection][2][0]) for beakonLocation in self.currentVariation]
        self.facingDirection += 1
        self.facingDirection %= 6
        self.currentVariation = [(beakonLocation[turningOperations[self.facingDirection][0][1]] * turningOperations[self.facingDirection][0][0], beakonLocation[turningOperations[self.facingDirection][1][1]] * turningOperations[self.facingDirection][1][0], beakonLocation[turningOperations[self.facingDirection][2][1]] * turningOperations[self.facingDirection][2][0]) for beakonLocation in self.currentVariation]

    def getRelativePositions(self):
        relativePositions = []
        for i, positionA in enumerate(self.currentVariation):
            theseRelativePositions = []
            for j, positionB in enumerate(self.currentVariation):
                if i != j:
                    theseRelativePositions.append((positionB[0]-positionA[0], positionB[1]-positionA[1], positionB[2]-positionA[2]))
            relativePositions.append((theseRelativePositions, positionA))
        return relativePositions

    def setAbsoluteLocation(self,x,y,z):
        self.currentVariation = [(position[0]+x, position[1]+y, position[2]+z) for position in self.currentVariation]
        self.offset = (x,y,z)

def getOverlappingExample(relativePositionsA, relativePositionsB):
    for beakonVetorsA in relativePositionsA:
        for beakonVetorsB in relativePositionsB:
            overlapCount = len(set(beakonVetorsA[0]) & set(beakonVetorsB[0]))
            if overlapCount > 10:
                return beakonVetorsA[1], beakonVetorsB[1]

def checkOverlap(scannerA, scannerB):
    scannerARelativePositions = scannerA.getRelativePositions()

    for rotationId in range(4):
        for directionId in range(6):
            scannerBRelativePositions = scannerB.getRelativePositions()
            overlappingExample = getOverlappingExample(scannerARelativePositions, scannerBRelativePositions)
            if overlappingExample:
                scannerB.setAbsoluteLocation(overlappingExample[0][0]-overlappingExample[1][0], overlappingExample[0][1]-overlappingExample[1][1], overlappingExample[0][2]-overlappingExample[1][2])
                return True
            scannerB.turn()
        scannerB.rotate()
    return False

startTime = time.time()

inputsRaw = [open("input.txt","r").read().split("\n\n")][0]

scanners = []

for i, inputRaw in enumerate(inputsRaw):
    scanResult = []
    for line in inputRaw.split("\n")[1:]:
        values = [int(x) for x in line.split(",")]
        scanResult.append((values[0], values[1], values[2]))
    scanners.append(Scanner(i, scanResult))

foundScannerIds = []
lastFoundScannerIds = [0]
newFoundScannerIds = []


while len(foundScannerIds) != len(scanners):
    for scannerAId in lastFoundScannerIds:
        for scannerBId in range(len(scanners)):
            if (scannerAId != scannerBId) and (scannerBId not in newFoundScannerIds) and (scannerBId not in lastFoundScannerIds) and (scannerBId not in foundScannerIds):
                if checkOverlap(scanners[scannerAId], scanners[scannerBId]):
                    newFoundScannerIds.append(scannerBId)

    for id in lastFoundScannerIds:
        foundScannerIds.append(id)
    lastFoundScannerIds = []

    for id in newFoundScannerIds:
        lastFoundScannerIds.append(id)
    newFoundScannerIds = []

allBeakons = []

for scannerId in foundScannerIds:
    for beakon in scanners[scannerId].currentVariation:
        allBeakons.append(beakon)

print(f"Solution 1: {len(set(allBeakons))}")

maxDistance = 0

scanners[0].offset = (0,0,0)

for beakonA in scanners:
    for beakonB in scanners:
        distance = abs(beakonA.offset[0] - beakonB.offset[0]) + abs(beakonA.offset[1] - beakonB.offset[1]) + abs(beakonA.offset[2] - beakonB.offset[2])
        if distance > maxDistance:
            maxDistance = distance

print(f"Solution 2: {maxDistance}")

print(time.time()-startTime)