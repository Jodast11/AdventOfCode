import re

input = [x.strip() for x in open("input.txt")]


codeLength = 0
memoryLength = 0
for line in input:
    codeLength += len(line)
    memoryLength += len(re.sub(r'\\x\w\w', "~", line.replace("\\\\","/").replace("\\\"","#")).replace("\"",""))

print(codeLength-memoryLength)