programm = [int(x) for x in [line.strip() for line in open("input.txt").readlines()][0].split(",")]

programm[1] = 12
programm[2] = 2

currentIndex = 0

while True:
    if programm[currentIndex] == 1:
        programm[programm[currentIndex+3]] = programm[programm[currentIndex + 1]] + programm[programm[currentIndex + 2]]
    elif programm[currentIndex] == 2:
        programm[programm[currentIndex+3]] = programm[programm[currentIndex + 1]] * programm[programm[currentIndex + 2]]
    elif programm[currentIndex] == 99:
        break
    else:
        print("Error")
        break

    currentIndex += 4

print(programm[0])