inputBuffer = [x for x in open("input.txt", "r").readlines()[0]]

uniqueLength = 14

for i in range(len(inputBuffer)-uniqueLength-1):
	if len(list(set(inputBuffer[i:i+uniqueLength]))) == uniqueLength:
		print(i+uniqueLength)
		break