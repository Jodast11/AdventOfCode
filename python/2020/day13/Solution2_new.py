import math

input = [x.strip() for x in open("Input.txt")]

busIds = [(int(busId) if busId != "x" else -1) for busId in input[1].split(",")]

def calcXY(inputA,inputB):
    a = [inputA]
    b = [inputB]
    q = [math.floor(inputA/inputB)]
    r = [inputA-(inputB*q[0])]

    while 0 not in r:
        a.append(b[-1])
        b.append(r[-1])
        q.append(math.floor(a[-1]/b[-1]))
        r.append(a[-1]-(b[-1]*q[-1]))

    x = [0]
    y = [1]

    for i in range(len(r)-2,-1,-1):
        x.append(y[-1])
        y.append(x[-2]-(q[i]*y[-1]))

    # print(f"x:{x[-1]}")
    # print(f"y:{y[-1]}")
    return y[-1]


print(busIds)

# numbers = [(2,3),(3,4),(2,5)]
# numbers = [(0,7),(12,13),(55,59),(25,31),(12,19)]

numbers = []
for i in range(len(busIds)):
    if busIds[i] != -1:
        numbers.append((busIds[i]-i, busIds[i]))

print(numbers)

M=1
for numberPair in numbers:
    M *= numberPair[1]

Mi = [int(M/pair[1]) for pair in numbers]

ei = []
for i in range(len(Mi)):
    ei.append(calcXY(numbers[i][1], Mi[i])*Mi[i])

x = 0
for i in range(len(ei)):
    x += ei[i]*numbers[i][0]

print(x%M)