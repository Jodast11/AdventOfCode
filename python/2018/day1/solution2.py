import os

def main():
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
        freqencyChanges = f.readlines()
        frequencysRead = [0]
        currentFrequency = 0
        while True:
            for changeStr in freqencyChanges:
                currentFrequency += int(changeStr.strip())
                if currentFrequency in frequencysRead:
                    print(currentFrequency)
                    return
                frequencysRead.append(currentFrequency)

main()