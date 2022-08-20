import re

input = [x.strip() for x in open("input.txt")][0]

pattern = re.compile("-?\d+")

matches = pattern.findall(input)

print(sum([int(match) for match in matches]))