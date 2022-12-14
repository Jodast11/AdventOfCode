lengths = [int(length.strip()) for length in open("input.txt","r").readlines()[0].split(",")]

listLength = 256

def getList(cycilcalList, startingPos, length):
    result = []
    for i in range(0, length):
        result.append(cycilcalList[(startingPos+i)%len(cycilcalList)])
    return result

def writeList(cyclicalList, startingPos, newList):
    for i, x in enumerate(newList):
        cyclicalList[(startingPos+i)%len(cyclicalList)] = x
    return cyclicalList

cycilcalList = [i for i in range(listLength)]

currentPosition = 0
skipSize = 0

for length in lengths:
    cycilcalList = writeList(cycilcalList, currentPosition, getList(cycilcalList, currentPosition, length)[::-1])
    currentPosition += length + skipSize
    skipSize += 1

print(cycilcalList[0]*cycilcalList[1])