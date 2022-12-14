instructions = [x.strip() for x in open("input.txt")]

leds = {}

def getRange(fromInstruction, toInstruction):
    positions = []
    xFrom, yFrom = fromInstruction.split(",")
    xTo, yTo = toInstruction.split(",")
    for x in range(int(xFrom),int(xTo)+1):
        for y in range(int(yFrom),int(yTo)+1):
            positions.append(str(x)+","+str(y))
    return positions

def executeOperation(position, operation):
    if position in leds.keys():
        leds[position] += operation
    else:
        leds[position] = operation
    if leds[position] < 0:
        leds[position] = 0

def prepareOpperation(opperation):
    opperationParts = opperation.split(" ")
    positions = getRange(opperationParts[-3], opperationParts[-1])
    for position in positions:
        executeOperation(position, -1 if "off" in opperation else (1 if "on" in opperation else 2))

for operation in instructions:
    prepareOpperation(operation)

totalBrightnes = 0

for ledPosition in leds:
    totalBrightnes += leds[ledPosition]

print(totalBrightnes)