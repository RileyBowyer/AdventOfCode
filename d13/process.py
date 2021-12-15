import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    dots = []
    folds = []
    while (line := f.readline().strip()) != "":
      dots.append(line.split(","))
    for line in f:
      line = line.strip().replace("fold along ", "")
      folds.append(line.split("="))
    return dots, folds


def processData(dots, folds):
  mat = [[0 for _ in range((int(max(dots, key=lambda x: int(x[0]))[0]) + 1))]
         for __ in range((int(max(dots, key=lambda x: int(x[1]))[1]) + 1))]

  for x, y in dots:
    mat[int(y)][int(x)] = 1

  for fold in folds:
    if fold[0] == "x":
      fold = int(fold[1])
      for item in mat:
        for x in range(fold, len(mat[0])):
          item[2 * fold - x] |= item[x]
      mat = [row[:fold] for row in mat]
    elif fold[0] == "y":
      fold = int(fold[1])
      for y in range(fold, len(mat)):
        for x in range(len(mat[0])):
          mat[2 * fold - y][x] |= mat[y][x]
      mat = mat[:fold]
  return mat


@utils.timeit
def process(data):
  dots, folds = data
  mat = processData(dots, folds[:1])
  return sum(x for row in mat for x in row)


@utils.timeit
def process2(data):
  dots, folds = data
  mat = processData(dots, folds)
  out = ""
  for row in mat:
    row = [str(x) for x in row]
    out += "\n" + "".join(row).replace("0", " ").replace("1", "@")
  return out


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
