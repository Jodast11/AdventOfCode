import os
import string

tree = {}

with open(f"{os.path.dirname(os.path.realpath(__file__))}/input.txt", "r") as f:
    lines = f.read().split("\n")