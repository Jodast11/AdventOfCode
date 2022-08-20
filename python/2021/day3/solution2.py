lines = [x.strip() for x in open("input.txt")]

def findMostCommon(data, index):
    return str(int([x[index] for x in data].count("1")>=[x[index] for x in data].count("0")))

def getValues(input, invert):
    allData = newData = input.copy()  
    for i in range(len(input[0])):
        allData = newData
        newData = []
        mostCommon = str(int(invert^bool(int(findMostCommon(allData,i)))))
        for data in allData:
            if data[i] == mostCommon:
                newData += [data]
        if len(newData) == 1:
            return int(newData[0],2)

print(int(getValues(lines,True))*int(getValues(lines,False)))