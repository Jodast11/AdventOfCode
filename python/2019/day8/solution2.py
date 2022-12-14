width = 25
hight = 6

input = [line.strip() for line in open("input.txt").readlines()][0]

layers = [[int(x) for x in input[i:i+(width*hight)]] for i in range(0,len(input), width * hight)]

decodedImage = []

for h in range(hight):
    newRow = ""
    for w in range(width):
        for l in range(len(layers)):
            pixel = layers[l][(h*width)+w]
            if pixel != 2:
                newRow += " " if pixel == 0 else "#"
                break
    decodedImage.append(newRow)    

for line in decodedImage:
    print(line)