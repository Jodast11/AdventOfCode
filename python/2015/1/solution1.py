with open("input.txt") as f:
    data = f.readlines()

level = 0
solutionTwoFound = False


for counter, char in enumerate(data[0]):
    # print(char)
    if char == "(":
        level+=1
    if char == ")":
        level-=1
    if level == -1 and not solutionTwoFound:
        print("Solution 2: "+str(counter+1))
        solutionTwoFound = True
        


print("Solution 1: "+str(level))
