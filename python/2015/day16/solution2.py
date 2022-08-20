linesAunts = [x.strip() for x in open("input.txt")]

linesKnownInformations = [x.strip() for x in open("input2.txt")]

def checkIfAuntFitsInformations(aunt, informations):
    for information in informations:
        if information in aunt:
            if information == "cats" or information == "trees":
                if aunt[information] <= informations[information]:
                    return False
            elif information == "pomeranians" or information == "goldfish":
                if aunt[information] >= informations[information]:
                    return False
            elif aunt[information] != informations[information]:
                return False
    return True

informations = {}
aunts = {}

for auntId, aunt in enumerate(linesAunts):
    newAunt = {}
    for information in aunt[aunt.find(":")+2:].split(", "):
        informationParts = information.split(": ")
        newAunt[informationParts[0]] = int(informationParts[1])
    aunts[auntId] = newAunt

for informationRaw in linesKnownInformations:
    information = informationRaw.split(": ")
    informations[information[0]] = int(information[1])

for auntId in aunts:
    if checkIfAuntFitsInformations(aunts[auntId], informations):
        print(auntId+1)
        break