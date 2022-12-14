class Folder:
	def __init__(self, folderName, prevFolder) -> None:
		self.name = folderName
		self.subElements = {}
		self.prevFolder = prevFolder

	def addElement(self, element):
		if element.name not in self.subElements:
			self.subElements[element.name] = element

	def getSize(self, path):
		if path in fileSizes:
			return fileSizes[path]
		else:
			size = 0
			for subElementName in self.subElements:
				subElement = self.subElements[subElementName]
				if type(subElement) == File:
					size += subElement.fileSize
				else:
					size += subElement.getSize(path+"/"+subElement.name)
			fileSizes[path] = size
			return size

class File:
	def __init__(self, fileName, fileSize) -> None:
		self.name = fileName
		self.fileSize = fileSize

terminalInput = open("input.txt", "r").readlines()

rootFolder = Folder("/", None)
currentDirectory = rootFolder

fileSizes = {}

for line in terminalInput:
	line = line.strip()
	if "$ cd" in line:
		targetDir = line.split(" ")[-1]
		if targetDir == "/":
			currentDirectory = rootFolder
		elif targetDir == "..":
			currentDirectory = currentDirectory.prevFolder
		else:
			currentDirectory = currentDirectory.subElements[targetDir]
		
	elif "$ ls" in line:
		pass
	elif "dir " in line:
		currentDirectory.addElement(Folder(line.split(" ")[-1], currentDirectory))
	else:
		parts = line.split(" ")
		currentDirectory.addElement(File(parts[1], int(parts[0])))

totalSpace = 70000000
requiredSpace = 30000000
freeSpace = totalSpace - rootFolder.getSize("/")
additionalRequiredSpace = requiredSpace-freeSpace

bestFolderSize = 69
bestFolderOvershot = totalSpace

for path in fileSizes:
    if fileSizes[path] >= additionalRequiredSpace:
        if (fileSizes[path] - additionalRequiredSpace) < bestFolderOvershot:
            bestFolderSize = fileSizes[path]
            bestFolderOvershot = fileSizes[path] - additionalRequiredSpace

print(bestFolderSize)