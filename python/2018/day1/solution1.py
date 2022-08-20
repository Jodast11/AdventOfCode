import os

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    print(eval(f.read().replace("\n","")))