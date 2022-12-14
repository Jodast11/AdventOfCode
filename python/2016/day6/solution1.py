import os

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    signals = f.read().split("\n")

rows = []

for signal in signals:
    for i, character in enumerate(signal):
        if len(rows) <= i:
            rows.append("")
        rows[i] += character

for row in rows:
    occurances = {x:row.count(x) for x in row}
    print(sorted(occurances, key=lambda x: occurances[x])[-1], end="")
print()