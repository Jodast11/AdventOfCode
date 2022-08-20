with open("Input.txt") as f:
    lines = f.read()
    
   

lines = lines.split("\n\n")

#print(lines) 

awnsers = []
awnserd = ""
counter = 0

for line in lines:
    awnsers.append(line.replace("\n","")) 

#print(awnsers)

for awnser in awnsers:
    for letter in awnser:
        if letter not in awnserd:
            awnserd = awnserd + letter
            counter += 1
    awnserd = ""

print(counter)
    