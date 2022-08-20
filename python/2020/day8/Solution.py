with open("Input.txt") as f:
    data = f.readlines()  #read the Input Data
    data_cleaned = []
    for line in data:   #remove the formating characters
        data_cleaned.append(line.strip())
        
accumulator = 0
positions = []

def execute(startPos):
    global accumulator
    global positions
    i = startPos
    while True:
        if i == len(data_cleaned):
            return True
            break
        if "acc" in data_cleaned[i]:
            accumulator += int(data_cleaned[i][4:9])
        if "jmp" in data_cleaned[i]:
            print(data_cleaned[i])
            print("Jumping from: "+str(i)+" to: "+str(i+int(data_cleaned[i][4:9])))
            if i+int(data_cleaned[i][4:9]) not in positions:
                positions.append(i+int(data_cleaned[i][4:9]))
                execute(i+int(data_cleaned[i][4:9]))
            else:
                print("Found endless loop")
                print(accumulator)
            break
        print(data_cleaned[i])
        i += 1
        
   
execute(0)
print(accumulator)