import math

memoryBanks = [int(memoryBank.strip()) for memoryBank in open("input.txt","r").read().split("\t")]

currentState = str(memoryBanks)
seenStates = []
cycles = 0

while currentState not in seenStates:
    seenStates.append(currentState)
    heaviestBankId = memoryBanks.index(max(memoryBanks))
    redistrebutionAmount = memoryBanks[heaviestBankId]
    maxRefillAmount = math.ceil(redistrebutionAmount/len(memoryBanks))
    maxRefillMemoryBanks = [(heaviestBankId+i+1)%len(memoryBanks) for i in range(redistrebutionAmount%len(memoryBanks))]
    memoryBanks[heaviestBankId] = 0
    x = 1 if not len(maxRefillMemoryBanks) else 0
    for id in range(len(memoryBanks)):
        if id in maxRefillMemoryBanks:
            memoryBanks[id] += maxRefillAmount+x
        else:
            memoryBanks[id] += maxRefillAmount-1+x
    currentState = str(memoryBanks)
    cycles += 1

print(cycles)