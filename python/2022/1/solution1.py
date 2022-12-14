callories = [[int(y.strip()) for y in x.split("\n")] for x in open("input.txt").read().split("\n\n")]

print(max([sum(x) for x in callories]))