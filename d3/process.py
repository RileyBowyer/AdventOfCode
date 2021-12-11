import sys
import os
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    return [list(line.strip()) for line in f]


@utils.timeit
def process(data):
  trees = 0
  col = 0
  for line in data:
    col %= len(line)
    if line[col] == "#":
      trees += 1
    col += 3
    
  return trees


@utils.timeit
def process2(data):
  steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
  trees = []
  for step in steps:
    tree = 0
    col = 0
    for line in data[::step[1]]:
      col %= len(line)
      if line[col] == "#":
        tree += 1
      col += step[0]
    trees.append(tree)
  print(trees)
  return np.prod(trees)


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
