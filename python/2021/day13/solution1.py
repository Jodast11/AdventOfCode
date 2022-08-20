def foldY(grid, y):
    newGrid = grid[0:y].copy()
    for i, line in enumerate(grid[y+1:]):
        for o, field in enumerate(line):
            if field:
                if len(grid[0:y])-i-1 >= 0:
                    newGrid[len(grid[0:y])-i-1][o] = 1
    return newGrid

def foldX(grid, x):
    newGrid = []
    for lineNr, line in enumerate(grid):
        newGrid.append(line[:int(len(line)/2)])
        for i, nr in enumerate(line[int(len(line)/2)+1:]):
            if nr:
                newGrid[lineNr][int(len(line)/2)-i-1] = 1  
    return newGrid

def printGrid(grid):
    for line in grid:
        newLine = ""
        for nr in line:
            newLine += "#" if nr else "."
        print(newLine)
        

inputParts = open("input.txt").read().split("\n\n")

# print(inputParts)

dotCords = []

for dotCord in inputParts[0].split("\n"):
    dotCords.append([int(x) for x in dotCord.split(",")])

sizeX = max([x[0] for x in dotCords])
sizeY = max([x[1] for x in dotCords])

paper = [[0 for i in range(sizeX+1)] for o in range(sizeY+1)]

for dotCord in dotCords:
    paper[dotCord[1]][dotCord[0]] = 1

# printGrid(foldX(foldY(paper, 7),5))
for instruction in inputParts[1].split("\n"):
    if instruction.split(" ")[-1][0] == "x":
        paper = foldX(paper,int(instruction.split(" ")[-1][2:]))
    else:
        paper = foldY(paper,int(instruction.split(" ")[-1][2:]))
    break

print(str(paper).count("1"))

# printGrid(paper)