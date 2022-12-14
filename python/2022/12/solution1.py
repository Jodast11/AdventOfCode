import string

class Field:
    def __init__(self, x, y, height) -> None:
        self.x = x
        self.y = y
        self.height = height
        self.previousField = None

    def __repr__(self) -> str:
        return f"{str((self.x, self.y))}"

    def isValidPosition(self, pos):
        global fieldHeight
        global fieldWidth
        x, y = pos
        return x >= 0 and y >= 0 and x<fieldHeight and y<fieldWidth

    def getAdjacent(self):
        result  = []
        x, y = self.x, self.y
        if self.isValidPosition((x-1, y)):
            result.append((x-1, y))
        if self.isValidPosition((x+1, y)):
            result.append((x+1, y))
        if self.isValidPosition((x, y-1)):
            result.append((x, y-1))
        if self.isValidPosition((x, y+1)):
            result.append((x, y+1))
        return result
    
    def flood(self):
        global newFloodFields
        adjacentFileds = self.getAdjacent()
        for adjacentFiled in adjacentFileds:
            if allFields[adjacentFiled].height <= self.height+1:
                if not allFields[adjacentFiled].previousField:
                    allFields[adjacentFiled].previousField = self
                    newFloodFields.append(allFields[adjacentFiled])

mapRaw = open("input.txt").read().split("\n")

heightMap = []
startPos = None
endPos = None

allFields = {}

for x, row in enumerate(mapRaw):
    heightMap.append([])
    for y, field in enumerate(row):
        if field == "E":
            endPos = (x,y)
            field = "z"
        if field == "S":
            startPos = (x,y)
            field = "a"
        newField = Field(x, y, string.ascii_lowercase.index(field))
        allFields[(x,y)] = newField

currentFloodFields = [allFields[startPos]]
newFloodFields = []

fieldHeight = len(mapRaw)
fieldWidth = len(mapRaw[0])

i = 0

while allFields[endPos] not in currentFloodFields:
    for floodField in currentFloodFields:
        floodField.flood()
    currentFloodFields = []
    currentFloodFields = newFloodFields
    newFloodFields = []

    i+= 1

print(i)