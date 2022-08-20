def runProgramm(programmInput, noun, verb):
    programm = [i for i in programmInput]
    programm[1] = noun
    programm[2] = verb

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
    
    return programm[0]

programm = [int(x) for x in [line.strip() for line in open("input.txt").readlines()][0].split(",")]

for noun in range(100):
    for verb in range(100):
        if runProgramm(programm, noun, verb) == 19690720:
            print((100 * noun) + verb)
            exit()