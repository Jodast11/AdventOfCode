lines = [x.strip() for x in open("input.txt")]

data = [[],[],[],[],[],[],[],[],[],[],[],[]]
finalGamma = ""
finalEpsilon = ""

for line in lines:
    for counter, character in enumerate(line):
        data[counter] += character

for line in data:
    finalGamma += str(int(line.count("1") > line.count("0")))
    finalEpsilon += str(int(line.count("1") < line.count("0")))

print(int(finalGamma, 2)*int(finalEpsilon, 2))