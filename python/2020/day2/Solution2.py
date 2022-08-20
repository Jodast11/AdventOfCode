import re
lines = []
with open("Input.txt") as f:
    lines = f.readlines()
    
valid = 0
pattern = '([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)'
for i in lines:
    match = re.search(pattern, i)
    pos1 = int(match.group(1))-1
    pos2 = int(match.group(2))-1
    char = match.group(3)
    password = match.group(4)
    if password[pos1] == char and password[pos2] != char:
        valid += 1
    if password[pos2] == char and password[pos1] != char:
        valid += 1
 

print(valid)