finalResults = {}

def createRanges(rangesRaw):
    rangesRaw = rangesRaw.split(" or ")
    ranges = []
    for rangeRaw in rangesRaw:
        ranges.append([int(rangeRaw.split("-")[0]),int(rangeRaw.split("-")[-1])])
    return ranges

def isFieldValid(fieldValue, possibleRanges):
    for possibleRange in possibleRanges:
        if fieldValue >= possibleRange[0] and fieldValue <= possibleRange[-1]:
            return True
    return False

def getPossibleFields(allFieldValues, allPosibleFieldNames, rules):
    global finalResults
    results = {}

    for fieldId, fieldValues in enumerate(allFieldValues):
        isPossible = [False not in [isFieldValid(value, rules[fieldName]) for value in fieldValues] for fieldName in allPosibleFieldNames]
        if isPossible.count(True) == 1:
            results[fieldId] = allPosibleFieldNames[isPossible.index(True)]
            allPosibleFieldNames.pop(allPosibleFieldNames.index(results[fieldId]))

    for result in results:
        finalResults[str(results[result])] = result

    if len(allPosibleFieldNames) != 0:
        getPossibleFields(allFieldValues, allPosibleFieldNames, rules)

inputRaw = open("Input.txt").read().split("\n\n")

rulesRaw = inputRaw[0].split("\n")

nearbyTickets = [[int(field) for field in ticket.split(",")] for ticket in inputRaw[2].split("\n")[1:]]

rules = {rule.split(": ")[0]:createRanges(rule.split(": ")[1]) for rule in rulesRaw}

myTicket = [[int(field) for field in ticket.split(",")] for ticket in inputRaw[1].split("\n")[1:]][0]

allRules = []

for fieldType in rules:
    for possibeRange in rules[fieldType]:
        allRules.append(possibeRange)

validNearbyTickets = []

for nearbyTicket in nearbyTickets:
    if not False in [isFieldValid(value, allRules) for value in nearbyTicket]:
        validNearbyTickets.append(nearbyTicket)

allFieldValues = [[validNearbyTicket[i] for validNearbyTicket in validNearbyTickets] for i in range(len(validNearbyTickets[0]))]

allPosibleFieldNames = [fieldName for fieldName in rules]

getPossibleFields(allFieldValues, allPosibleFieldNames, rules)

result = 1

for posibleFieldName in [fieldName for fieldName in rules]:
    if posibleFieldName.startswith("departure"):
        result *= myTicket[finalResults[posibleFieldName]]

print(result)