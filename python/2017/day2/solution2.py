seperator = "\t"

input = [[int(number) for number in line.strip().split(seperator)] for line in open("input.txt","r").read().split("\n")]

def getData(spreadsheet):
    result = 0
    for row in spreadsheet:
        for indexOne, numberOne in enumerate(row):
            for indexTwo, numberTwo in enumerate(row):
                if indexOne != indexTwo:
                    if numberOne % numberTwo == 0:
                        result += numberOne / numberTwo
    return int(result)

print(getData(input))
