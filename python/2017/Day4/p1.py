with open("input.txt") as f:
    lines = f.readlines()

linesCleaned = []

for line in lines:
    linesCleaned.append(line.replace("\n",""))

invalid = 0

for line in linesCleaned:
    parts = line.split(" ")
    print(parts)
    print("Entering new")
    for part in parts:
        print(parts.count(part))
        if parts.count(part) > 1:
            invalid += 1
            print("breaking")
            break

print(len(lines)-invalid)