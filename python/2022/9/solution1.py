class Rope():
	def __init__(self) -> None:
		self.head = [0,0]
		self.tail = [0,0]
		self.positionsVisited = []
		self.positionsVisited.append(str(self.tail[0])+"|"+str(self.tail[1]))

	def isStreched(self): #Checks if head and tail arn't connected
		return not (self.tail[0] >= self.head[0]-1 and self.tail[0] <= self.head[0]+1 and self.tail[1] >= self.head[1]-1 and self.tail[1] <= self.head[1]+1)

	def moveHead(self, direction):
		xMove, yMove = direction
		if xMove:
			for _ in range(abs(xMove)):
				self.head[0] += 1 if xMove > 0 else -1
				if self.isStreched():
					self.pullTail()
		else:
			for _ in range(abs(yMove)):
				self.head[1] += 1 if yMove > 0 else -1
				if self.isStreched():
					self.pullTail()

		#print(self.head, self.tail)


	def pullTail(self):
		xHead, yHead = self.head
		xTail, yTail = self.tail

		xMove = -1 if xHead < xTail else (0 if xHead == xTail else 1)
		yMove = -1 if yHead < yTail else (0 if yHead == yTail else 1)

		self.tail[0] += xMove
		self.tail[1] += yMove
		self.positionsVisited.append(str(self.tail[0])+"|"+str(self.tail[1]))		

instructions = open("input.txt", "r").read().split("\n")

r = Rope()

for instruction in instructions:
	direction, amount = instruction.split(" ")
	amount = int(amount)
	if direction == "R":
		r.moveHead((amount,0))
	if direction == "L":
		r.moveHead((-amount,0))
	if direction == "U":
		r.moveHead((0,amount))
	if direction == "D":
		r.moveHead((0,-amount))

print(len(list(set(r.positionsVisited))))