with open("input.txt") as f:
    lines = [x for x in f.read().split("\n")]

def checkIfAnagram(str1, str2):
    for letter in str1:
        posLetter = str2.find(letter)
        if posLetter == -1:
            return False
        str2 = str2[0:posLetter]+str2[posLetter+1:]
    return True

invalid = 0

for line in lines:
    foundAnagram = False
    parts = line.split(" ")
    for index, part1 in enumerate(parts):
        for part2 in parts[index+1:]:
            if len(part1) == len(part2):
                if checkIfAnagram(part1, part2):
                    foundAnagram = True
                    invalid += 1
                    break
        if foundAnagram:
            break
                    
print(len(lines)-invalid)