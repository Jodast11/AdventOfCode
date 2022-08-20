input = open("input.txt").read()
lines = input.split("\n\n")

def checkIfWon(field):
    for row in field:
        if row.count(-1) == 5:
            return True
    for i in range(5):
        if [x[i] for x in field].count(-1) == 5:
            return True
    return False

def replaceNr(field, number):
    newField = []
    for line in field:
        newLine = []
        for place in line:
            newLine.append(place if place != number else -1)
        newField.append(newLine)
    return newField

def doCyclesUntilAllWon(numbersDraw, fields):
    boardsAlreadyWon = []
    for numberDrawn in numbersDraw:
        for i in range(len(fields)):
            fields[i] = replaceNr(fields[i],numberDrawn)
            if i not in boardsAlreadyWon:
                if checkIfWon(fields[i]):
                    boardsAlreadyWon.append(i)
            if len(boardsAlreadyWon) == len(fields):
                return numberDrawn, fields[i]

def calculateScore(finalNumber, finalField):
    sumUnmarked = 0
    for row in finalField:
        for cell in row:
            sumUnmarked += cell if cell != -1 else 0
    return finalNumber * sumUnmarked

numbersDrawn = [int(x) for x in lines.pop(0).split(",")]

fields = []

for field in lines:
    rows = field.split("\n")
    newField = []
    for row in rows:
        newRow = []
        for value in row.split(" "):
            if value != "":
                newRow.append(int(value))
        newField.append(newRow)
    fields.append(newField)

finalNumber, finalField = doCyclesUntilAllWon(numbersDrawn,fields)
print(calculateScore(finalNumber, finalField))