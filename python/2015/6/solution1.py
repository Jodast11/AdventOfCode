import time

startTime = time.time()

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

def appendOperation(position, operation):
    if position in leds.keys():
        leds[position].append(operation)
    else:
        leds[position] = [operation]

def prepareOpperation(opperation):
    opperationParts = opperation.split(" ")
    positions = getRange(opperationParts[-3], opperationParts[-1])
    for position in positions:
        appendOperation(position, 0 if "off" in opperation else (1 if "on" in opperation else 2))

def getStatus(operations):
    if operations[0] == 0:
        return False
    if operations[0] == 1:
        return True
    else:
        if len(operations) == 1:
            return True
        else:
            return not getStatus(operations[1:])

for operation in instructions:
    prepareOpperation(operation)

litLeds = 0

for led in leds:
    if getStatus(leds[led][::-1]):
        litLeds += 1

print(litLeds)

print(time.time()-startTime)