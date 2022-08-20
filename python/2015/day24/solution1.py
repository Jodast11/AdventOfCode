import math

impossibleNumbers = []

def getPosibilities(target, remainingNumbers):
    global impossibleNumbers

    if target in impossibleNumbers:
        return []

    remainingNumbers.sort(reverse = True)
    
    posibilities = []
    for number in remainingNumbers:
        if number == target:
            posibilities.append([number])
        else:
            if number > target:
                continue
            else:
                for posibilitie in getPosibilities(target-number, remainingNumbers[:remainingNumbers.index(number)]+remainingNumbers[remainingNumbers.index(number)+1:]):
                    posibilities.append([number] + posibilitie)

    if len(posibilities) == 0:
        impossibleNumbers.append(target)
    
    uniques = []
    for posibilitie in posibilities:
        posibilitie.sort()
        if posibilitie not in uniques:
            uniques.append(posibilitie)
    return uniques

def getQE(x):
    return math.prod(x)

inputs = [int(input) for input in open("input.txt","r").read().split("\n")]

#3 Gruppen -> gleich schwer
#1. Gruppe -> sowenige packete wie möglich
#1. Gruppe -> kleinste prod

allPosibilities = {}

for posibilitie in getPosibilities(int(sum(inputs) / 4), inputs):
    if len(posibilitie) in allPosibilities:
        allPosibilities[len(posibilitie)].append(posibilitie)
    else:
        allPosibilities[len(posibilitie)] = [posibilitie]

smallest = allPosibilities[min(allPosibilities.keys())]


smallest.sort(key=getQE)
print(getQE(smallest[0]))