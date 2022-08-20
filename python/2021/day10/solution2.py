def checkIfLineValid(line): #returns none if line is vailid else it returns the unexpected character
    openingPossibilitys = "([{<"
    closingPosibilities = ")]}>"

    previousBlocks = []

    for character in line:
        if character in openingPossibilitys:
            previousBlocks.append(openingPossibilitys.index(character))
        else:
            expectedChar = previousBlocks.pop(-1)
            if closingPosibilities[expectedChar] != character:
                return character
    return

def getMissingCharacters(line): #returns none if line is vailid else it returns the unexpected character
    openingPossibilitys = "([{<"
    closingPosibilities = ")]}>"

    previousBlocks = []
    missingCharacters = ""

    for character in line:
        if character in openingPossibilitys:
            previousBlocks.append(openingPossibilitys.index(character))
        else:
            previousBlocks.pop(-1)

    for missingCharacter in previousBlocks:
        missingCharacters += closingPosibilities[missingCharacter]
    
    return missingCharacters[::-1]

code = [x.strip() for x in open("input.txt")]

cleanedCode = []

for line in code:   
    returnValue = checkIfLineValid(line)
    if returnValue == None:
        cleanedCode.append(line)

scores = []

for line in cleanedCode:
    newScore = 0
    for missingCharacter in getMissingCharacters(line):
        newScore = newScore * 5
        newScore += ")]}>".index(missingCharacter) + 1
    scores.append(newScore)

scores.sort()
print(scores[int(len(scores)/2)])