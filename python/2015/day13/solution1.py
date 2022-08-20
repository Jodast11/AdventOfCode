def getBestHappines(prefferences, peopleSeated, happines, currentPerson):
    if len(peopleSeated) == len(prefferences): #if every location has been visited
        return happines + prefferences[peopleSeated[0]][currentPerson] + prefferences[currentPerson][peopleSeated[0]] #first and last person
    
    nextPersonHappines = []
    for person in prefferences[currentPerson]:
        if person not in peopleSeated:
            newHappines = happines + prefferences[currentPerson][person] + preferences[person][currentPerson]
            nextPersonHappines.append(getBestHappines(prefferences, peopleSeated + [person], newHappines, person))
    return max(nextPersonHappines)

lines = [x.strip() for x in open("input.txt")]

preferences = {}

for line in lines:
    parts = line.split(" ")

    source = parts[0][0]
    destination = parts[-1][0]
    amount = int(parts[3])
    happinesType = 1 if parts[2] == "gain" else -1

    if source not in preferences:
        preferences[source] = {destination: amount*happinesType}
    else:
        preferences[source][destination] = amount*happinesType

happineses = []
for firstPerson in preferences:
    happineses.append(getBestHappines(preferences, [firstPerson], 0, firstPerson))

print(max(happineses))