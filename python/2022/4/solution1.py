inputRaw = [x.strip() for x in open("input.txt").readlines()]

""" def isContainedInOtherRange(targetRange, targetRangeId, ranges):
    targetRangeStart = targetRange[0]
    targetRangeLength = targetRange[1]
    for rangeId, range in enumerate(ranges):
        if ranges[rangeId][0] > targetRangeStart:
            break
        if rangeId == targetRangeId:
            continue
        if range[0] + range[1] <= targetRangeStart + targetRangeLength:
            return True
    return False """

def containEachother(pair):
    elvA = pair[0]
    elvB = pair[1]
    if ((elvA[0] <= elvB[0]) and (elvA[1] >= elvB[1])) or ((elvB[0] <= elvA[0]) and (elvB[1] >= elvA[1])):
        return True
    return False

elves = []

for line in inputRaw:
    elv = []
    for linePart in line.split(","):
        rangeParts = linePart.split("-")
        elv.append([int(rangeParts[0]), int(rangeParts[1])])
    elves.append(elv)

print([containEachother(pair) for pair in elves].count(True))