class Rope():
	def __init__(self, id) -> None:
		self.nextRope = None
		self.id = id
		self.head = [0,0]
		self.tail = [0,0]
		self.positionsVisited = []
		self.positionsVisited.append(str(self.tail[0])+"|"+str(self.tail[1]))

	def isStreched(self): #Checks if head and tail arn't connected
		return not (self.tail[0] >= self.head[0]-1 and self.tail[0] <= self.head[0]+1 and self.tail[1] >= self.head[1]-1 and self.tail[1] <= self.head[1]+1)

	def moveHead(self, direction):
		xMove, yMove = direction
		for _ in range(max([abs(xMove), abs(yMove)])):
			self.head[0] += 1 if xMove > 0 else (-1 if xMove else 0)
			self.head[1] += 1 if yMove > 0 else (-1 if yMove else 0)
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
		if self.nextRope:
			self.nextRope.moveHead((xMove, yMove))

		

instructions = open("input.txt", "r").read().split("\n")

ropes = []

for i in range(9):
	r = Rope(i)
	ropes.append(r)

for i, rope in enumerate(ropes):
	if i+1 != len(ropes):
		rope.nextRope = ropes[i+1]

for instruction in instructions:
	direction, amount = instruction.split(" ")
	amount = int(amount)
	if direction == "R":
		ropes[0].moveHead((amount,0))
	if direction == "L":
		ropes[0].moveHead((-amount,0))
	if direction == "U":
		ropes[0].moveHead((0,amount))
	if direction == "D":
		ropes[0].moveHead((0,-amount))

print(len(list(set(ropes[-1].positionsVisited))))

print(ropes[-1].positionsVisited)