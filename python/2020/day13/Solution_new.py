import math

input = [x.strip() for x in open("Input.txt")]

arival = int(input[0])

busIds = [(int(busId) if busId != "x" else -1) for busId in input[1].split(",")]
while -1 in busIds:
    busIds.remove(-1)

earliestId = -1
earliestDeparture = 9999999

for busId in busIds:
    departuresBefore = math.floor(arival / busId)
    depatureTime = (departuresBefore + 1) * busId
    if depatureTime < earliestDeparture:
        earliestDeparture = depatureTime
        earliestId = busId

print(earliestId* (earliestDeparture-arival))