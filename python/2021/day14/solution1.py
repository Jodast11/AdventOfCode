inputParts = open("input.txt").read().split("\n\n")

currentFormula = inputParts[0]

insertionRulesRaw = inputParts[1].split("\n")
insertionRules = {}

for insertionRuleRaw in insertionRulesRaw:
    parts = insertionRuleRaw.split(" -> ")
    insertionRules[parts[0]] = parts[1]

for i in range(10):
    nextFormula = ""
    for i in range(len(currentFormula)-1):
        nextFormula += currentFormula[i]
        if currentFormula[i:i+2] in insertionRules:
            nextFormula += insertionRules[currentFormula[i:i+2]]
    nextFormula += currentFormula[-1]   
    currentFormula = nextFormula

temp = nextFormula

allLetters = []

while len(temp) != 0:
    allLetters.append(temp[0])
    temp = temp.replace(allLetters[-1],"")

occurances = [nextFormula.count(letter) for letter in allLetters]
print(max(occurances)-min(occurances))



        