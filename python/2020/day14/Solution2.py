with open("Input.txt") as f: #open the imput file
    lines = [x for x in f.read().split("\n")] #split its lines and save it into lines

memory_map = {}

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
    
def writeToMemoryAddress(mask,address_int,value_int):
    address_bin = convertToBinary(address_int)
    value_bin = convertToBinary(value_int)
    
    
def findPossibleAddresses(address_bin, mask):
    number_of_xs = 0
    possibleXs = []
    possibleAddresses = []
    
    for character in mask:
        if character == "X":
            number_of_xs += 1
    possibleXs.append("0b0")
    for i in range(1,(2**number_of_xs)):
        possibleXs.append(bin(int(possibleXs[i-1],2)+int("1",2)))
    
    maxLen=len(possibleXs[-1])
    for counter,content in enumerate(possibleXs):
        if len(content)<maxLen:
            possibleXs[counter] = content[:2]+(maxLen-len(content))*"0"+content[2:]
    
    for counter,content in enumerate(possibleXs):
        possibleXs[counter] = content[2:]
        
    #print(possibleXs)
    
    for x in possibleXs:
        addressInProcess = ""
        i = 0
        for counter,character in enumerate(mask):   
            if character == "0":
                addressInProcess = addressInProcess+address_bin[counter]
            if character == "1":
                addressInProcess = addressInProcess+"1"
            if character == "X":
                addressInProcess=addressInProcess+x[i]
                i+=1
        possibleAddresses.append(addressInProcess)
     
    #print(possibleAddresses)
    
    for counter,content in enumerate(possibleAddresses):
        possibleAddresses[counter] = convertToInt(content)
    #print(possibleAddresses)
    return possibleAddresses
    
def createMemoryMapping():
    #addresses=[]
    global memory_map
    a = 0
    for anweisung in lines:
        if "mask" in anweisung:
            mask = anweisung[7:]
        else:
            for i in findPossibleAddresses(convertToBinary(int(anweisung[int(anweisung.index("[")+1):int(anweisung.index("]"))])),mask):
                #addresses.append(i)
                if i not in memory_map:
                    memory_map.update({i:a})
                    a+=1
    #print(memory_map)




createMemoryMapping() 

mask = ""
memory = [""]*100000
for anweisung in lines:
    if "mask" in anweisung:
        mask = anweisung[7:]
    else:
        for i in findPossibleAddresses(convertToBinary(int(anweisung[int(anweisung.index("[")+1):int(anweisung.index("]"))])),mask):
            memory[memory_map[i]] =  anweisung[anweisung.index("=")+1:]

result = 0
for i in memory:
    if i != "":
        result += int(i)
        
print(memory)
print()     
print(result)

             
    

        
        
        

     



