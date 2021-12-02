import os.path
file = os.path.dirname('/Users/jaden/Downloads/input.txt/')

with open(file) as r:
    lines = r.readlines()

lines = [line.strip() for line in lines]

print(lines)
