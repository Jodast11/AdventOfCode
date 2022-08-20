with open("Input.txt") as f:
    data = f.readlines()  #read the Input Data
    data_cleaned = []
    for line in data:   #remove the formating characters
        data_cleaned.append(line.strip())
        
def isNumberValid(index):
    number = data_cleaned[index]
    keys = []
    print(number)
    for i in range(25):
        keys.append(data_cleaned[index-1-i])
    print(keys)
    for i in keys:
        print("Number at index is : "+str(int(data_cleaned[index])))
        print("Number i is: "+str(int(i)))
        print("Number needet is: "+str(int(data_cleaned[index])-int(i)))
        print()
        if str(int(data_cleaned[index])-int(i)) in keys:
            return True
    return False

i = 25
while isNumberValid(i):
    i += 1

print(str(i)+" : "+str(data_cleaned[i]))

invalid_number = int(data_cleaned[i])

startRange = 0
endRange = 0
values = []

def findSequence(inv_number):
    global startRange
    global endRange
    global values
    counter = 0
    for i in range(len(data_cleaned)):
        for a in range(len(data_cleaned)):
            for b in range(a-i):
                counter += int(data_cleaned[b+i])
                values.append(int(data_cleaned[b+i]))
                if counter == inv_number:
                    print()
                    print(i)
                    print(a)
                    print()
                    startRange = i
                    endRange = a
                    return True
            print(counter)
            counter = 0
            values = []
    return False
        
print(findSequence(invalid_number))

print()

print(values)

def addHighestAndLowest():
    global values
    values.sort()
    return values[0]+values[len(values)-1]

print("Result: "+str(addHighestAndLowest()))        
    