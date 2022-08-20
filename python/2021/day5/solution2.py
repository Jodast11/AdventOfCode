lines = [x.strip() for x in open("input.txt")]

def printField(field):
    for line in field:
        newLine = ""
        for cell in line:
            newLine += str(cell) if cell != 0 else "."
        print(newLine)

inputs = []

for line in lines:
    parts = line.split(" -> ")
    newEntry = []
    for part in parts:
        cords = part.split(",")
        newCords = (int(cords[0]),int(cords[1]))
        newEntry.append(newCords)
    inputs.append(newEntry)

horizontalLines = [] #all coordinates, that represent a horizontal line
verticalLines = [] #all coordinates, that represent a vertical line
topLeftDiagonals = []
topRightDiagonals = []

#assign the cords into different groups depending on their orientation
for cords in inputs:
    # print(cords)
    cords1 = cords[0]
    cords2 = cords[1]
    
    if cords1[0] == cords2[0]: #verical line
        if cords1[1] > cords2[1]:
            cords1, cords2 = cords2, cords1
        verticalLines += [[cords1, cords2]]

    elif cords[0][1] == cords[1][1]: #horizontal line
        if cords1[0] > cords2[0]:
            cords1, cords2 = cords2, cords1
        horizontalLines += [[cords1, cords2]]

    else: #diagonal line
        if cords1[0] > cords2[0]:
            cords1, cords2 = cords2, cords1
        # print([[cords1, cords2]])
        if cords1[1] > cords2[1]:
            topRightDiagonals += [[cords1, cords2]]
        else:
            topLeftDiagonals += [[cords1, cords2]]


field = [[0 for j in range(1000)] for i in range(1000)]

for cords in verticalLines:
    for y in range(cords[0][1],cords[1][1]+1):
        field[y][cords[0][0]] += 1

for cords in horizontalLines:
    for x in range(cords[0][0],cords[1][0]+1):
        field[cords[0][1]][x] += 1

for cords in topRightDiagonals:
    for i in range(cords[1][0]-cords[0][0]+1):
        field[cords[0][1]-i][cords[0][0]+i] += 1

for cords in topLeftDiagonals:
    for i in range(cords[1][0]-cords[0][0]+1):
        field[cords[0][1]+i][cords[0][0]+i] += 1

#determine the max number of line overlaps
print(sum([str(field).count(str(i)) for i in range(max([max(line) for line in field])+1)][2:]))