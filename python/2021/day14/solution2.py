import string

inputParts = open("input.txt").read().split("\n\n")

currentFormula = inputParts[0]

insertionRulesRaw = inputParts[1].split("\n")
insertionRules = {}

for insertionRuleRaw in insertionRulesRaw:
    parts = insertionRuleRaw.split(" -> ")
    insertionRules[parts[0]] = parts[1]

pairs = {}

for i in range(len(currentFormula)-1):
    if currentFormula[i:i+2] in pairs:
        pairs[currentFormula[i:i+2]] += 1  
    else:
        pairs[currentFormula[i:i+2]] = 1

for i in range(40):
    newPairs = {}
    for pair in pairs:
        if pair in insertionRules:
            if pair[0] + insertionRules[pair] in newPairs:
                newPairs[pair[0] + insertionRules[pair]] += pairs[pair]
            else:
                newPairs[pair[0] + insertionRules[pair]] = pairs[pair]
            
            if insertionRules[pair] + pair[1] in newPairs:
                newPairs[insertionRules[pair] + pair[1]] += pairs[pair]
            else:
                newPairs[insertionRules[pair] + pair[1]] = pairs[pair]
        else:
            if pair in newPairs:
                newPairs[pair] += pairs[pair]
            else:
                newPairs[pair] = pairs[pair]
    pairs = newPairs
    # print(pairs)

occurances = []

for character in string.ascii_uppercase:
    counter = 0
    for pair in pairs:
        if pair[0] == character:
            counter += pairs[pair]
    if inputParts[0][-1] == character:
        counter += 1
    occurances.append(counter)

minOccurance = 99999999999999999

for occuranceCount in occurances:
    if occuranceCount != 0 and occuranceCount < minOccurance:
        minOccurance = occuranceCount

print(max(occurances)-minOccurance)
print(occurances)