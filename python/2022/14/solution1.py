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
            if type(element) == int:
                element = [element]
            if type(packetB[i]) == int:
                packetB[i] = [packetB[i]]
            result = compare([element, packetB[i]])
            if result < 2:
                return result
    if len(packetB) > len(packetA):
        return 1
    return 2


pairsRaw = open("input.txt","r").read().split("\n\n")

solution = 0

for i, pairRaw in enumerate(pairsRaw):
    pair = [json.loads(x) for x in pairRaw.split("\n")]
    if compare(pair) == 1:
        solution += i+1

print(solution)