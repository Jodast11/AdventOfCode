with open("Input.txt") as f:
    lines = f.read()

lines = lines.split("\n\n")

possibleAwnsers = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]

#print(lines)
counter = 0
awnserCounter = 0

for line in lines:
    awnser = line.split("\n")
    #print(awnser)
    #print()
    for possibleAwnser in possibleAwnsers:
        for i in range(len(awnser)):
            if possibleAwnser in awnser[i]:
                awnserCounter += 1
        if awnserCounter == len(awnser):
            counter += 1
        awnserCounter = 0
    awnser = []
    
print(counter)

    