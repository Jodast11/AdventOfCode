lines = [x.strip() for x in open("input.txt")]

allData = []
uniquesDetected = 0

for line in lines:
    allData.append([y.split(" ") for y in line.split(" | ")])

for data in allData:
    for output in data[1]:
        if (len(output) > 1 and len(output) < 5) or len(output) == 7:
            uniquesDetected += 1

print(uniquesDetected)
