callories = [[int(y.strip()) for y in x.split("\n")] for x in open("input.txt").read().split("\n\n")]

elfCalories = [sum(x) for x in callories]
elfCalories.sort()

print(sum([elfCalories[-i] for i in range(1,4)]))