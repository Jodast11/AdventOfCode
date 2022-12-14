inputRaw = [x.strip() for x in open("input.txt").readlines()]

def overlap(pair):
    elvA = pair[0]
    elvB = pair[1]
    if (elvA[1] < elvB[0]) or (elvB[1] < elvA[0]):
        return False
    return True

elves = []

for line in inputRaw:
    elv = []
    for linePart in line.split(","):
        rangeParts = linePart.split("-")
        elv.append([int(rangeParts[0]), int(rangeParts[1])])
    elves.append(elv)

print([overlap(pair) for pair in elves].count(True))