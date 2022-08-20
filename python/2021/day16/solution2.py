import math

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

def calculateSolution(package):
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
        return pValue, origPackageLength-len(package)
    else:
        results = []
        lengthTypeId = package[0]
        package = package[1:]
        if lengthTypeId == "0":
            length = int(package[:15],2)
            package = package[15:]
            lengthShortend = 0
            while lengthShortend != length:
                returnedSum, newLengthShortend = calculateSolution(package)
                results.append(returnedSum)
                lengthShortend += newLengthShortend
                package = package[newLengthShortend:]
            # return totalSum+pVersion, origPackageLength - len(package)
        else:
            length = int(package[:11],2)
            package = package[11:]
            lengthShortend = 0
            for i in range(length):
                returnedSum, newLengthShortend = calculateSolution(package)
                results.append(returnedSum)
                lengthShortend += newLengthShortend
                package = package[newLengthShortend:]
            # return totalSum+pVersion, origPackageLength - len(package)

        if pType == 0:
            return sum(results), origPackageLength - len(package)
        if pType == 1:
            return math.prod(results), origPackageLength - len(package)
        if pType == 2:
            return min(results), origPackageLength - len(package)
        if pType == 3:
            return max(results), origPackageLength - len(package)
        if pType == 5:
            return int(results[0] > results[1]), origPackageLength - len(package)
        if pType == 6:
            return int(results[0] < results[1]), origPackageLength - len(package)
        if pType == 7:
            return int(results[0] == results[1]), origPackageLength - len(package)


            

input = hexToBin([line.strip() for line in open("input.txt").readlines()][0])

sum, lengthShortend = calculateSolution(input)
print(sum)