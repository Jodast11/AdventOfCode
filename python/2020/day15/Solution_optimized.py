import time

time_start = time.time()
with open("Input.txt") as f: #open the imput file
    lines = [x for x in f.read().split(",")] #split its lines and save it into lines

numbers=[]
numbers_spoken = {}

for counter,content in enumerate(lines):
    numbers.append(int(content))
    numbers_spoken.update({content:int(counter)})
    numbers_spoken.update({content+"_old":int(counter)})

def hasNumberBeenSpoken(number,index):
    if str(number) in numbers_spoken:
        #print("1")
        if numbers_spoken[str(number)+"_old"] != index:
            #print("2")
            return True
    return False
    
def getLastPositionOfNumber(number):
    return numbers_spoken[str(number)+"_old"]

lastNumber = numbers[-1]
     
for i in range(len(lines),30000000):
    if hasNumberBeenSpoken(lastNumber,i-1):
        #print("Adding difference")
        numberToAdd = (i-1)-getLastPositionOfNumber(lastNumber)
        lastNumber = numberToAdd
        if str(numberToAdd) in numbers_spoken:
            numbers_spoken.update({str(numberToAdd)+"_old":numbers_spoken[str(numberToAdd)]})
            numbers_spoken.update({str(numberToAdd):i})
        else:
            numbers_spoken.update({str(numberToAdd):i})
            numbers_spoken.update({str(numberToAdd)+"_old":i})
    else:
        #print("Adding 0")
        lastNumber = 0
        if "0" in numbers_spoken: 
            numbers_spoken.update({"0_old":numbers_spoken["0"]})
            numbers_spoken.update({"0":i})
        else:
            numbers_spoken.update({"0":i})
            numbers_spoken.update({"0_old":i})
            
#print(numbers)
#print(numbers_spoken)
print(lastNumber)
print(time.time()-time_start)
        
        
        

     



