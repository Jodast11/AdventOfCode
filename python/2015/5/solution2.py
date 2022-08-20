f = open("input.txt", "r")
input_raw = f.readlines() 
f.close()

input = []

for line in input_raw:
    input.append(line.strip())

print(input)