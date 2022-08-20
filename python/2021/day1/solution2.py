lines = [int(x.strip()) for x in open("input.txt")]

lastSum = 99999
timesIncreased = 0

for i in range(len(lines)-2) : timesIncreased, lastSum = timesIncreased + (sum(lines[i:i+3]) > lastSum) if timesIncreased != None else 0, sum(lines[i:i+3])

print(timesIncreased)