treeMap = [[int(y) for y in x.strip()] for x in open("input.txt", "r").readlines()]

def getScenicScore(treeLocation):
    x, y = treeLocation
    thisTreeHight = treeMap[x][y]
    up = [treeMap[offset][y] for offset in range(x-1, -1, -1)]
    down = [treeMap[offset][y] for offset in range(x+1, len(treeMap))]
    left = [treeMap[x][offset] for offset in range(y-1, -1, -1)]
    right = [treeMap[x][offset] for offset in range(y+1, len(treeMap[0]))]
    
    upCount = 0
    for treeHight in up:
        upCount += 1
        if treeHight >= thisTreeHight:
            break

    downCount = 0
    for treeHight in down:
        downCount += 1
        if treeHight >= thisTreeHight:
            break

    leftCount = 0
    for treeHight in left:
        leftCount += 1
        if treeHight >= thisTreeHight:
            break

    rightCount = 0
    for treeHight in right:
        rightCount += 1
        if treeHight >= thisTreeHight:
            break

    return upCount * downCount * leftCount * rightCount

print(max([max([getScenicScore((x,y)) for y in range(len(treeMap[0]))]) for x in range(len(treeMap))]))