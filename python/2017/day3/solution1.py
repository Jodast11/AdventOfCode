input = 9

def getRingMax(ring):
    ringMax = 1
    for i in range(ring):
        ringMax += 2*((1 + (i*2))+2)+(2*(1 + (i*2)))

    return ringMax

def getRing(number):
    ringMax = 1
    ring = 0
    while getRingMax(ring) < number:
        ring += 1
    return ring

def getCenterNumbers(ring):
    ringStart = getRingMax(ring-1)+1
    centerNumbers = [ringStart + (ring - 1)]
    for i in range(3):
        centerNumbers.append(centerNumbers[-1]+(2*ring))
    return centerNumbers

def getRingCornerNumbers(ring):
    ringCenterNumbers = getCenterNumbers(ring)
    return [number+ring for number in ringCenterNumbers]

def getOffset(number):
    ring = getRing(number)
    ringCenterNumbers = getCenterNumbers(ring)
    ringCornerNumbers = getRingCornerNumbers(ring)
    if number <= ringCenterNumbers[0]:
        return ring + (ringCenterNumbers[0] - number)
    if number <= ringCornerNumbers[0]:
        return ring + (number - ringCenterNumbers[0])

    if number <= ringCenterNumbers[1]:
        return ring + (ringCenterNumbers[1] - number)
    if number <= ringCornerNumbers[1]:
        return ring + (number - ringCenterNumbers[1])

    if number <= ringCenterNumbers[2]:
        return ring + (ringCenterNumbers[2] - number)
    if number <= ringCornerNumbers[2]:
        return ring + (number - ringCenterNumbers[2])

    if number <= ringCenterNumbers[3]:
        return ring + (ringCenterNumbers[3] - number)
    if number <= ringCornerNumbers[3]:
        return ring + (number - ringCenterNumbers[3])


print(getOffset(265149))