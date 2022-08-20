with open("Input.txt") as f:
    parts = f.read().split("\n")

all_instructions = []
   
for part in parts:
    instructions_cleaned = []
    instruction_active = ""
    instructions = [] 
    char_prev = ""   
    for char in part:
        if len(instruction_active) > 1:
            instructions.append(instruction_active)
            instruction_active = ""
            char_prev = ""
        if char_prev == "":
            instruction_active = instruction_active + char
            char_prev = char
        else:
            if char_prev == "n" or char_prev == "s":
                if char == "w" or char == "e":
                    instruction_active = instruction_active + char
                    char_prev = char
                else:
                    if len(instruction_active) > 0:
                        instructions.append(instruction_active)
                        instruction_active = ""
                        char_prev = ""
                        instruction_active = char
            else:
                if len(instruction_active) > 0:
                    instructions.append(instruction_active)
                    instruction_active = ""
                    char_prev = ""
                    instruction_active = char

    for instruction in instructions:
        if instruction == "n":
            instructions_cleaned.append(0) 
        if instruction == "ne":
            instructions_cleaned.append(1) 
        if instruction == "e":
            instructions_cleaned.append(2) 
        if instruction == "se":
            instructions_cleaned.append(3) 
        if instruction == "s":
            instructions_cleaned.append(4) 
        if instruction == "sw":
            instructions_cleaned.append(5) 
        if instruction == "w":
            instructions_cleaned.append(6) 
        if instruction == "nw":
            instructions_cleaned.append(7) 
    
    all_instructions.append(instructions_cleaned)
    
def getCords(array):
    x = 0
    y = 0
    for instruction in array:
        if instruction == 0: #n
            y+=2
        if instruction == 1: #ne
            x+=1
            y+=1
        if instruction == 2: #e
            x+=2
        if instruction == 3: #se
            x+=1
            y-=1
        if instruction == 4: #s
            y-=2
        if instruction == 5: #sw
            x-=1
            y-=1
        if instruction == 6: #w
            x-=2
        if instruction == 7: #nw
            x+=-1
            y+=1
    # print(x)
    # print(y)
    return x,y

# Strings = []
        
# for i in all_instructions:
    # x,y = getCords(i)
    # string = str(x)+"|"+str(y)
    # if string in Strings:
        # print("Already Preasent")
        # Strings.remove(string)
    # else:
        # Strings.append(string)
  
# print(all_instructions)  
# print(Strings)
# print(len(Strings))

print(getCords([2,3,6]))
        

