strategys = [x.strip() for x in open("input.txt").readlines()]

#A: Rock
#B: Paper
#C: Scisors

gameValues = {"AX": 3+0, "AY": 1+3, "AZ": 2+6, "BX": 1+0, "BY": 2+3, "BZ": 3+6, "CX": 2+0, "CY": 3+3, "CZ": 1+6}

totalScore = 0

for singleStrategy in strategys:
    totalScore += gameValues[singleStrategy.replace(" ", "")]

print(totalScore)