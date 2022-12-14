inputRaw = open("input.txt", "r").read()

containersRaw, instructionsRaw = inputRaw.split("\n\n")

containersRaw = containersRaw.split("\n")

containers = ["","","","","","","","",""]

for x in containersRaw[:-1][::-1]:
	for containerId, containerRaw in enumerate([x[i:i+4] for i in range(0, len(x), 4)]):
		container = containerRaw.replace("[","").replace("]","").replace(" ","")
		if container:
			containers[containerId] += container

instructionsRaw = instructionsRaw.split("\n")
instructionsRaw = instructionsRaw[:-1]
instructions = []

for instructionRaw in instructionsRaw:
	_, amount, _, fromStack, _, toStack = instructionRaw.split(" ")
	instructions.append((int(amount), int(fromStack), int(toStack)))

def applyInstruction(instruction):
	global containers
	amount, fromStack, toStack = instruction
	instructionContainers = containers[fromStack-1][-amount:]
	containers[fromStack-1] = containers[fromStack-1][:-amount]
	containers[toStack-1] += instructionContainers

for instruction in instructions:
	applyInstruction(instruction)

print("".join([x[-1] for x in containers]))
