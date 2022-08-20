def findBasinSize(basinMap, y, x): #returns basinMap, basinFieldsFound
    basinFieldsFound = 0
    newBasinMap = basinMap.copy()
    if newBasinMap[y][x]:
        newBasinMap[y][x] = 0
        basinFieldsFound += 1
        if y+1 < len(basinMap):
            newBasinMap, newFieldsFound = findBasinSize(basinMap,y+1,x)
            basinFieldsFound += newFieldsFound
        if y-1 >= 0:
            newBasinMap, newFieldsFound = findBasinSize(basinMap,y-1,x)
            basinFieldsFound += newFieldsFound
        if x-1 >= 0:
            newBasinMap, newFieldsFound = findBasinSize(basinMap,y,x-1)
            basinFieldsFound += newFieldsFound
        if x+1 < len(basinMap[0]):
            newBasinMap, newFieldsFound = findBasinSize(basinMap,y,x+1)
            basinFieldsFound += newFieldsFound
    return newBasinMap, basinFieldsFound

dangerMapRaw = [x.strip() for x in open("input.txt")]

dangerMap = []

for lineRaw in dangerMapRaw:
    line = []
    for nr in lineRaw:
        line.append(int(nr))
    dangerMap.append(line)

basinMap = [[0 for i in range(len(dangerMap[0]))] for j in range(len(dangerMap))]

for y, line in enumerate(dangerMap):
    for x, danger in enumerate(line):
        if danger != 9:
            basinMap[y][x] = 1

allBasinSizes = []

for y in range(len(basinMap)):
    for x in range(len(basinMap[y])):
        basinMap, basinSize = findBasinSize(basinMap, y, x)
        if basinSize != 0:
            allBasinSizes.append(basinSize)

big3Size = 1
for i in range(3):
    big3Size *= allBasinSizes.pop(allBasinSizes.index(max(allBasinSizes)))

print(big3Size)