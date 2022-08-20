def countNeigbours(field, x, y):
    count = 0
    for searchY in range(-1,2):
        for searchX in range(-1,2):
            if y + searchY >= 0 and x + searchX >= 0 and y + searchY < len(field) and x + searchX < len(field):
                count += field[y+searchY][x+searchX]
    count -= field[y][x]
    return count

initialStatesRaw = [line.strip() for line in open("input.txt")]

initialStates = []

for line in initialStatesRaw:
    newLine = []
    for character in line:
        newLine.append(0 if character == "." else 1)
    initialStates.append(newLine)

initialStates[0][0] = 1
initialStates[-1][0] = 1
initialStates[0][-1] = 1
initialStates[-1][-1] = 1

field = initialStates.copy()

for i in range(100):
    newField = []
    for y, line in enumerate(field):
        newLine = []
        for x, state in enumerate(line):
            if (x == 0 and y == 0) or (x == 0 and y == len(field)-1) or (x == len(field)-1 and y == 0) or (x == len(field)-1 and y == len(field)-1):
                newLine.append(1)
            else:
                suroundingOn = countNeigbours(field,x,y)
                if state:
                    if suroundingOn < 2 or suroundingOn > 3:
                        newLine.append(0)
                    else:
                        newLine.append(1)
                else:
                    if suroundingOn == 3:
                        newLine.append(1)
                    else:
                        newLine.append(0)
        newField.append(newLine)
    field = newField.copy()

print(sum([str(line).count("1") for line in field]))
# print(field)
