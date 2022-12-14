import json

def compare(pair): #0:wrong order 1:right order 2:same
    packetA, packetB = pair
    for i, element in enumerate(packetA):
        if len(packetB) == i:
            return 0
        if type(element) == int and type(packetB[i]) == int:
            if element < packetB[i]:
                return 1
            if element > packetB[i]:
                return 0
        else:
            x = [element] if type(element) == int else element
            y = [packetB[i]] if type(packetB[i]) == int else packetB[i]
            result = compare([x, y])
            if result < 2:
                return result
    if len(packetB) > len(packetA):
        return 1
    return 2


inputRaw = open("input.txt","r").read().replace("\n\n", "\n").split("\n")

inputObjects = []

inputObjects.append([[2]])
inputObjects.append([[6]])

for inputObject in inputRaw:
    inputObjects.append(json.loads(inputObject))

swapped = True
while swapped:
    swapped = False
    for i in range(len(inputObjects)-1):
        pair = inputObjects[i], inputObjects[i+1]
        result = compare(pair)
        if result == 0:
            swapped = True
            inputObjects[i] = pair[-1]
            inputObjects[i+1] = pair[0]
            
print((inputObjects.index([[2]])+1)*(inputObjects.index([[6]])+1))