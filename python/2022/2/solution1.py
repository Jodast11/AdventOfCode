strategys = [x.strip() for x in open("input.txt").readlines()]

gameValues = {"AX": 1+3, "AY": 2+6, "AZ": 3+0, "BX": 1+0, "BY": 2+3, "BZ": 3+6, "CX": 1+6, "CY": 2+0, "CZ": 3+3}

totalScore = 0

for singleStrategy in strategys:
    totalScore += gameValues[singleStrategy.replace(" ", "")]

print(totalScore)