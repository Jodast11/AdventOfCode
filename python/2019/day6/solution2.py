import time

orbits = {}

currentTickPlanets = []

planetsTicked = []

input = [line.strip() for line in open("input.txt").readlines()]

start = ""
goal = ""

for orbit in input:
    planets = orbit.split(")")

    #get start and goal planet
    if planets[1] == "YOU":
        start = planets[0]
    if planets[1] == "SAN":
        goal = planets[0]

    if planets[1] in orbits:
        orbits[planets[1]].append(planets[0])
    else:
        orbits[planets[1]] = [planets[0]]

    if planets[0] in orbits:
        orbits[planets[0]].append(planets[1])
    else:
        orbits[planets[0]] = [planets[1]]

currentTickPlanets = [start]
planetsTicked = [start]

tickNr = 0

startTime = time.time()

while goal not in currentTickPlanets:
    tickNr += 1
    nextTickPlanets = []
    for currentTickPlanet in currentTickPlanets:
        for surroundingPlanet in orbits[currentTickPlanet]:
            if surroundingPlanet not in planetsTicked:
                nextTickPlanets.append(surroundingPlanet)
                planetsTicked.append(surroundingPlanet)
    currentTickPlanets = nextTickPlanets

print(time.time()-startTime)

print(tickNr)