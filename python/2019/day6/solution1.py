orbits = {}

knownOrbits = {"COM":0}

def countOrbits(orbits, planet):
    global knownOrbits
    if orbits[planet] not in knownOrbits.keys():
        countOrbits(orbits, orbits[planet])
    knownOrbits[planet] = knownOrbits[orbits[planet]] + 1

input = [line.strip() for line in open("input.txt").readlines()]

for orbit in input:
    planets = orbit.split(")")
    if planets[1] in orbits:
        orbits[planets[1]].append(planets[0])
    else:
        orbits[planets[1]] = planets[0]

for planet in orbits:
    countOrbits(orbits, planet)

checksum = 0

for planet in knownOrbits:
    checksum += knownOrbits[planet]

print(checksum)