with open("Input.txt") as f: #open the imput file
    lines = [x for x in f.read().split("\n")] #split its lines and save it into lines

#print(lines)

def convertToBinary(number_int):
    number_bin = bin(number_int)
    number_bin = number_bin[2:]
    while len(number_bin) < 36:
        number_bin = "0"+number_bin
    return number_bin
    
def convertToInt(number_bin):
    return int(number_bin,2)
    
def addToMask(number_bin, mask):
    Result = ""
    for i in range(len(mask)):
        if mask[i] != "X":
            Result = Result + mask[i]
        else:
            Result = Result + number_bin[i]
    return Result
    
mask = ""
memory = [""]*75000
for anweisung in lines:
    if "mask" in anweisung:
        mask = anweisung[7:]
        #print(mask)
    else:
        memory[int(anweisung[int(anweisung.index("[")+1):int(anweisung.index("]"))])] = convertToInt(addToMask(convertToBinary(int(anweisung[anweisung.index("=")+1:])),mask))
        
#print(memory)
result = 0
for i in memory:
    if i != "":
        result += int(i)
     
print(result)
        
        
        

     



