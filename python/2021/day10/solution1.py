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

code = [x.strip() for x in open("input.txt")]

solution = 0

for line in code:   
    returnValue = checkIfLineValid(line)
    if returnValue != None:
        if returnValue == ")":
            solution += 3
        if returnValue == "]":
            solution += 57
        if returnValue == "}":
            solution += 1197
        if returnValue == ">":
            solution += 25137

print(solution)