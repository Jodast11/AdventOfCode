def hexToBin(input):
    output = ""
    for char in input:
        if char == "0":
            output += "0000"
        elif char == "1":
            output += "0001"
        else:
            output += char.replace("2","0010").replace("3","0011").replace("4","0100").replace("5","0101").replace("6","0110").replace("7","0111").replace("8","1000").replace("9","1001").replace("A","1010").replace("B","1011").replace("C","1100").replace("D","1101").replace("E","1110").replace("F","1111")     
    return output

def calculateSumOfSubpackages(package):
    # print("Package: "+package)
    origPackageLength = len(package)
    pVersion = int(package[:3],2)
    package = package[3:]
    pType = int(package[:3],2)
    package = package[3:]
    if pType == 4:
        valueBin = ""
        while True:
            if package[0] == "1":
                valueBin += package[1:5]
                package = package[5:]
            else:
                valueBin += package[1:5]
                package = package[5:]
                break
        pValue = int(valueBin,2)
        # print("Value "+str(pValue))
        # print("shortend by "+str(origPackageLength-len(package)))
        return pVersion, origPackageLength-len(package)
    else:
        lengthTypeId = package[0]
        package = package[1:]
        if lengthTypeId == "0":
            length = int(package[:15],2)
            # print("Length: "+package[:15])
            package = package[15:]
            lengthShortend = 0
            totalSum = 0
            # print("Contains packages with total length of "+str(length))
            while lengthShortend != length:
                returnedSum, newLengthShortend = calculateSumOfSubpackages(package)
                totalSum += returnedSum
                lengthShortend += newLengthShortend
                package = package[newLengthShortend:]
            # print("shortend by "+str(lengthShortend))
            return totalSum+pVersion, origPackageLength - len(package)
        else:
            length = int(package[:11],2)
            package = package[11:]
            lengthShortend = 0
            totalSum = 0
            # print("Contains "+str(length)+" packages")
            for i in range(length):
                returnedSum, newLengthShortend = calculateSumOfSubpackages(package)
                totalSum += returnedSum
                lengthShortend += newLengthShortend
                package = package[newLengthShortend:]
            # print("shortend by "+str(lengthShortend))
            return totalSum+pVersion, origPackageLength - len(package)


            

input = hexToBin([line.strip() for line in open("input.txt").readlines()][0])

sum, lengthShortend = calculateSumOfSubpackages(input)
print(sum)