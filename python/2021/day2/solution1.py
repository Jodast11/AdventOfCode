lines = [x.strip().replace("forward ","f").replace("up ","u").replace("down ","d") for x in open("input.txt")]

depth = 0
horizontal = 0

for line in lines:
    if "f" in line:
        horizontal += int(line[1:])
    if "u" in line:
        depth -= int(line[1:])
    if "d" in line:
        depth += int(line[1:])

# print(lines)
print(depth*horizontal)