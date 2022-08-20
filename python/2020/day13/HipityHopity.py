from math import prod


def readNotes(inpath="input.txt"):
    with open(inpath, "r") as infile:
        lines = infile.read().splitlines()
        return lines[1].split(",")

def chiRem(n, a):
    sum = 0
    product = prod(n)  #calculates the product of all numbers in the array n
    for i, j in zip(n, a):
        p = product // i
        sum += j * modInv(p, i) * p
    return sum % product


def modInv(a, b):  #returnes the rest of the division of a through b
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def part2(ids):
    n = []
    a = []
    for i, t in enumerate(ids):
        if t != "x":
            n.append(int(t))
            a.append(int(t)-i)
    return chiRem(n, a)


def main():
    earliest, ids = readNotes()
    print(f"Part 1: {part1(earliest, ids)}\nPart 2: {part2(ids)}")


main()