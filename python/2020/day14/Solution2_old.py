with open("Input.txt") as f: #open the imput file
    lines = [x for x in f.read().split("\n")] #split its lines and save it into lines

memory = [""]*75000

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
    possibleMasks = []
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
    
    #print("Possible X: ")    
    for content in possibleXs:
        #print(content)
        maskInProcess=""
        i=2
        for character in mask:
            if character == "X":
                try:
                    maskInProcess=maskInProcess+content[i]
                    i+=1
                except:
                    maskInProcess=maskInProcess+"0"
                    i+=1
            else:
                maskInProcess=maskInProcess+character
        possibleMasks.append(maskInProcess)    
        
    for possibleMask in possibleMasks:
        print("A: "+address_bin)
        print("M: "+possibleMask)
        addressInProcess = ""
        for counter, character in enumerate(possibleMask):
            if character == "0":
                addressInProcess = addressInProcess+address_bin[counter]
            if character == "1":
                addressInProcess = addressInProcess+"1"
        possibleAddresses.append(addressInProcess)
        print("E: "+addressInProcess)
        print()
        
        
            
        
findPossibleAddresses("000000000000000000000000000000101010","000000000000000000000000000000X1001X")
        
        
            
    

        
        
        

     



