input = "1321131112"
output = ""

cycles = 50

for i in range(cycles):
    currentNumber = input[0]
    count = 0
    for nr in input:
        if nr == currentNumber:
            count += 1
        else:
            output += str(count) + currentNumber
            currentNumber = nr
            count = 1
    output += str(count) + currentNumber
    input = output
    output = ""

print(len(input))