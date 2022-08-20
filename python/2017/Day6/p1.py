memorryBank = [10, 9, 8, 7, 6, 5, 4, 3, 1, 1, 0, 15, 14, 13, 11, 12]
previousBanks = ""

steps = 0

while previousBanks.find(str(memorryBank)) < 0:
    previousBanks += str(memorryBank)
    maxNum = max(memorryBank)
    indexOfMaxNum = memorryBank.index(maxNum)
    memorryBank[indexOfMaxNum] = 0
    curIndex = indexOfMaxNum + 1
    for i in range(maxNum):
        if curIndex == len(memorryBank):
            curIndex = 0
        memorryBank[curIndex] += 1
        curIndex += 1
    steps += 1

print(memorryBank)

print(steps)