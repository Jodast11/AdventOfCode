inputBuffer = [x for x in open("input.txt", "r").readlines()[0]]

for i in range(len(inputBuffer)-3):
	if len(list(set(inputBuffer[i:i+4]))) == 4:
		print(i+4)
		break