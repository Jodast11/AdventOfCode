glowsquidsRaw = [int(y) for y in [x.strip() for x in open("input.txt")][0].split(",")]

def daylyCycle(glowsquids):
    newGlowsquids = {x:0 for x in range(9)}
    for age in glowsquids:
        if age == 0:
            #spawn new glowsquid with age 8
            #reset age to 6
            newGlowsquids[8] += glowsquids[age]
            newGlowsquids[6] += glowsquids[age]
        else:
            #decrease age by one
            newGlowsquids[age-1] += glowsquids[age]
    return newGlowsquids
        
def countGlowsquids(glowsquids):
    total = 0
    for age in glowsquids:
        total += glowsquids[age]
    return total

glowsquids = {x:glowsquidsRaw.count(x) for x in range(9)}

for i in range(80):
    glowsquids = daylyCycle(glowsquids)

print(countGlowsquids(glowsquids))
