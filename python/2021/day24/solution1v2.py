import math
import time

def doStep(z,div1,add1,add2,inp):
    x = int(((z%26)+add1) != inp) #0 if (z%26)+add1 == inp
    y = 26 if x else 1
    z = math.floor(z/div1)*y
    y = inp+add2 if x else 0
    return z+y #return z if x == 0

input = open("input.txt").read().split("inp w\n")[1:]

div1 = []
add1 = []
add2 = []

for line in input:
    instructions = line.split("\n")
    div1.append(int(instructions[3].split(" ")[-1]))
    add1.append(int(instructions[4].split(" ")[-1]))
    add2.append(int(instructions[14].split(" ")[-1]))

print(add1)
print(div1)
print(add2)

startTime = time.time()
inp = [1,3,5,7,9,2,4,6,8,9,9,9,9,9]

z = 0

for i in range(len(input)):
    z = doStep(z,div1[i],add1[i],add2[i],inp[i])

print(z)
