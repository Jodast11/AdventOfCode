with open("Input.txt") as f: #open the imput file
    lines = [x for x in f.read().split("\n")] #split its lines and save it into lines

valid = []
tser=0

def findValid():
    global valid
    valid_raw = []
    for counter, content in enumerate(lines):
        if counter<20:
            start1 = int(content[content.index(":")+1:content.index("-")])
            end1 = int(content[content.index("-")+1:content.index(" ",content.index("-"))])
            start2 = int(content[content.index(" or ")+4:content.index("-",content.index(" or "))])
            end2 = int(content[content.index("-",content.index(" or "))+1:])
            for i in range(start1,end1+1):
                valid_raw.append(i)
            for i in range(start2,end2+1):
                valid_raw.append(i)
    valid = list(set(valid_raw))
    valid.sort()
    #print(valid)
    
findValid()

for i in range(25,len(lines)):
    #print(lines[i])
    line = lines[i].split(",")
    for i in line:
        if int(i) not in valid:
            tser += int(i)
            print("Addinng invalid: "+i)
       
print(tser)