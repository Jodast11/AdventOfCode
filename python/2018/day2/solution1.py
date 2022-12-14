import os
import string

threes = 0
twos = 0

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    lines = f.read().split("\n")

for line in lines:
    twoCounted = False
    threeCounted = False
    for letter in string.ascii_lowercase:
        count = line.count(letter)
        if count == 2 and not twoCounted:
            twos += 1
            twoCounted = True
        if count == 3 and not threeCounted:
            threes += 1
            threeCounted = True

print(twos*threes)