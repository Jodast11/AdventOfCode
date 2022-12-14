width = 25
hight = 6

input = [line.strip() for line in open("input.txt").readlines()][0]

layers = [[int(x) for x in input[i:i+(width*hight)]] for i in range(0,len(input), width * hight)]

zeroCounts = [layer.count(0) for layer in layers]

minZeroCountLayer = layers[zeroCounts.index(min(zeroCounts))]

print(minZeroCountLayer.count(1)*minZeroCountLayer.count(2))