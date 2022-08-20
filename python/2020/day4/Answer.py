import re
linesRaw = []
linesRaw2 = ""
lines = []

with open("Input.txt") as f:
    linesRaw = f.readlines()
for i in linesRaw:
    linesRaw2=linesRaw2+i    
lines = linesRaw2.split("\n\n")

valid = 0

for i in range(len(lines)):
    if "byr" in lines[i] and "ecl" in lines[i] and "iyr" in lines[i] and "eyr" in lines[i] and "hgt" in lines[i] and "hcl" in lines[i] and "ecl" in lines[i] and "pid" in lines[i]:
        valid += 1

print(lines)
#print(linesRaw)    
print(valid)