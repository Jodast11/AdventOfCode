import re

def clean(input):
    return input.replace("*","\\").replace("'","\"")

input = [x.strip() for x in open("input.txt")]

unencodedLength = 0
encodedLength = 0

for line in input:
    unencodedLength += len(line)
    encodedLength += len(clean("\""+line.replace("\"","*'").replace("\\","\\\\")+"\""))

print(encodedLength-unencodedLength)