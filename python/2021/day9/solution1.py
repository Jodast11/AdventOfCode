dangerMapRaw = [x.strip() for x in open("input.txt")]

dangerMap = []

for lineRaw in dangerMapRaw:
    line = []
    for nr in lineRaw:
        line.append(int(nr))
    dangerMap.append(line)

# print(dangerMap)

overallRiskLevel = 0

for y, line in enumerate(dangerMap):
    for x, danger in enumerate(line):
        smallerCount = 0
        if y+1 < len(dangerMap):
            if dangerMap[y][x] < dangerMap[y+1][x]:
                smallerCount += 1
        else:
            smallerCount += 1

        if y-1 >= 0:
            if dangerMap[y][x] < dangerMap[y-1][x]:
                smallerCount += 1
        else:
            smallerCount += 1

        if x+1 < len(line):
            if dangerMap[y][x] < dangerMap[y][x+1]:
                smallerCount += 1
        else:
            smallerCount += 1

        if x-1 >= 0:
            if dangerMap[y][x] < dangerMap[y][x-1]:
                smallerCount += 1
        else:
            smallerCount += 1
            
        if smallerCount == 4:
            overallRiskLevel += 1 + danger

print(overallRiskLevel)