inputChars = [length for length in open("input.txt","r").readlines()[0]]

def getList(cycilcalList, startingPos, length):
    result = []
    for i in range(0, length):
        result.append(cycilcalList[(startingPos+i)%len(cycilcalList)])
    return result

def writeList(cyclicalList, startingPos, newList):
    for i, x in enumerate(newList):
        cyclicalList[(startingPos+i)%len(cyclicalList)] = x
    return cyclicalList

def knotHash(inputChars, rounds=1, listLength=256):
    cycilcalList = [i for i in range(listLength)]

    currentPosition = 0
    skipSize = 0

    for _ in range(rounds):
        for inputChar in inputChars:
            cycilcalList = writeList(cycilcalList, currentPosition, getList(cycilcalList, currentPosition, inputChar)[::-1])
            currentPosition += inputChar + skipSize
            skipSize += 1

    return cycilcalList

def toHexStr(nr):
    hexStr = '{0:x}'.format(nr)
    return hexStr if len(hexStr) == 2 else "0"+hexStr

def calculateDenseHash(sparseHash):
    result = []
    for i, x in enumerate(sparseHash):
        if not i % 16:
            result.append(0)
        result[-1] ^= x
    return "".join([toHexStr(x) for x in result])

inputBytes = [ord(inputChar) for inputChar in inputChars] + [17, 31, 73, 47, 23]

print(calculateDenseHash(knotHash(inputBytes, rounds=64)))