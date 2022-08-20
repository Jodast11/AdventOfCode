seperator = "\t"

input = [[int(number) for number in line.strip().split(seperator)] for line in open("input.txt","r").read().split("\n")]

def getChecksum(spreadsheet):
    checksum = 0
    for row in spreadsheet:
        checksum += max(row) - min(row)
    print(checksum)

getChecksum(input)