import string
import time

def increment(passwordIntInput):
    passwordInt = passwordIntInput.copy()[::-1]
    newPasswordInt = []
    if passwordInt[0] == 25:
        newPasswordInt.append(0)
        for newLetterInt in increment(passwordInt[1:][::-1])[::-1]:
            newPasswordInt.append(newLetterInt)
    else:
        newPasswordInt.append(passwordInt[0]+1)
        for newLetterInt in passwordInt[1:]:
            newPasswordInt.append(newLetterInt)
    return newPasswordInt[::-1]
        
def toString(intArray):
    alpahabet = string.ascii_lowercase
    result = ""
    for integer in intArray:
        result += alpahabet[integer]
    return result

def checkIfValid(passwordInt):
    invalidInts = [8,14,11]
    pairCount = 0
    prevInt = 26
    sequenceLength = 0
    validCheck1 = False
    foundPairLastRound = False
    for integer in passwordInt:
        #invalid int
        if integer in invalidInts:
            return False

        #two pairs
        if prevInt == integer and not foundPairLastRound:
            pairCount += 1
            foundPairLastRound = True
        else:
            foundPairLastRound = False

        #sequence of three
        if integer == prevInt + 1:
            sequenceLength += 1
        else:
            sequenceLength = 0
        prevInt = integer
        if sequenceLength == 2:
            validCheck1 = True

    if not validCheck1 or pairCount < 2:
        return False  
    return True

def skipUnwanted(passwordInt):
    invalidInts = [8,14,11]
    result = []
    for i, integer in enumerate(passwordInt):
        if integer in invalidInts:
            result.append(increment([integer])[0])
            for j in range(len(passwordInt)-i-1):
                result.append(0)
            break
        else:
            result.append(integer)
    return result

def getNextValid(passwordInt):
    while not checkIfValid(passwordInt):
        passwordInt = increment(passwordInt)
        passwordInt = skipUnwanted(passwordInt)
    return passwordInt

startTime = time.time()

alpahabet = string.ascii_lowercase

input = [alpahabet.index(letter) for letter in "hxbxwxba"]

print(toString(getNextValid(increment(getNextValid(input)))))

print(time.time()-startTime)

# print(toString(skipUnwanted(input)))


# print(checkIfValid(input))

