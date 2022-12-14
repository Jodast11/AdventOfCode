treeMap = [[int(y) for y in x.strip()] for x in open("input.txt", "r").readlines()]

visibilitys = []

#Left to Right
for row in treeMap:
	rowVisibility = []
	heighestTree = -1
	for tree in row:
		if tree > heighestTree:
			heighestTree = tree
			rowVisibility.append(True)
		else:
			rowVisibility.append(False)
	visibilitys.append(rowVisibility)

#Right to Left
for x, row in enumerate(treeMap):
	heighestTree = -1
	for y, tree in enumerate(row[::-1]):
		if tree > heighestTree:
			heighestTree = tree
			visibilitys[x][-(y+1)] = True

#Up to Down
heighestTrees = [-1]*len(treeMap[0])
for x, row in enumerate(treeMap):
	for y, tree in enumerate(row):
		if tree > heighestTrees[y]:
			heighestTrees[y] = tree
			visibilitys[x][y] = True

#Down to Up
heighestTrees = [-1]*len(treeMap[0])
for x, row in enumerate(treeMap[::-1]):
	for y, tree in enumerate(row):
		if tree > heighestTrees[y]:
			heighestTrees[y] = tree
			visibilitys[-(x+1)][y] = True

print(sum([row.count(True) for row in visibilitys]))