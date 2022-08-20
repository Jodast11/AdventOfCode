with open("Input.txt") as f: #open the imput file
    lines = [x for x in f.read().replace(" ","").split("\n")] #split its lines and save it into lines
    
#print(lines)

result = 0

def solve(stringToSolve):
    result = 0
    operation = 0 #0:anfangswert 1:plus 2:minus 3:mal 
    skip = 0
    for counter, char in enumerate(stringToSolve):
        if skip != 0:
            skip -= 1
        else:
            if char == "(":
                opening = 0
                closing = 0
                for i in range(counter,len(stringToSolve)):
                    if stringToSolve[i] == "(":
                        opening += 1
                    if stringToSolve[i] == ")":
                        closing += 1
                    if opening == closing:
                        print()
                        print("Entering Recursion: ")
                        
                        if operation == 0:
                            result = solve(stringToSolve[counter+1:i])
                        if operation == 1:
                            result += solve(stringToSolve[counter+1:i])
                        if operation == 2:
                            result -= solve(stringToSolve[counter+1:i])
                        if operation == 3:
                            result *= solve(stringToSolve[counter+1:i])
                        
                        print("Skipping: "+str(len(stringToSolve[counter+1:i])+2))
                        skip = len(stringToSolve[counter+1:i])+1
                        break
                        
            if char == "+":
                print("Setting Operation to Adding")
                operation = 1
            if char == "-":
                print("Setting Operation to Subtrakting")
                operation = 2
            if char == "*":
                print("Setting Operation to Multipling")
                operation = 3
                
            if char != "(" and char != ")" and char != "+" and char != "-" and char != "*":
                if operation == 0:
                    print("Setting starting value: "+char)
                    result = int(char)
                if operation == 1:
                    print("Adding: "+char)
                    result += int(char)
                if operation == 2:
                    print("Subtrakting: "+char)
                    result -= int(char)
                if operation == 3:
                    print("Multipling: "+char)
                    result *= int(char)
      
    print("The result is: "+str(result))
    return result
        

for line in lines:
    result += solve(line)
    
print(result)

# print(solve("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2".replace(" ","")))
