import re

lines = [x.strip() for x in open("input.txt")]

ingredients = {}

for line in lines:
    parts = re.split(": |, ", line)
    ingredients[parts[0]] = [part.split(" ")[-1] for part in parts[1:]]

print(ingredients)