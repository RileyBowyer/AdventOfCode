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
    return [[int(elem) for elem in line.strip()] for line in f]


def findLowest(data):
  lowPoints = []
  neighbours = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  for rIndex, row in enumerate(data):
    for cIndex, elem in enumerate(row):
      neighbourPoints = []
      for r, c in neighbours:
        try:
          if rIndex + r < 0 or cIndex + c < 0:
            continue
          neighbourPoints.append(data[rIndex + r][cIndex + c])
        except IndexError:
          continue
      if all([point > elem for point in neighbourPoints]):
        lowPoints.append((elem, rIndex, cIndex))
  return lowPoints


@utils.timeit
def process(data):
  riskSum = 0
  for point, r, c in findLowest(data):
    riskSum += point + 1
  return riskSum


@utils.timeit
def process2(data):
  basins = []
  neighbours = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
  for pInit, rInit, cInit in findLowest(data):
    basin = [(rInit, cInit)]
    toCheck = [(pInit, rInit + rNeighbour, cInit + cNeighbour)
               for rNeighbour, cNeighbour in neighbours]
    for point, r, c in toCheck:
      try:
        if r < 0 or c < 0:
            continue
        nPoint = data[r][c]
      except IndexError:
        continue
      if data[r][c] > point and data[r][c] < 9 and (r, c) not in basin:
        basin.append((r, c))
        toCheck.extend([(nPoint, r + rNeighbour, c + cNeighbour)
                        for rNeighbour, cNeighbour in neighbours])
    basins.append(basin)
  basins = sorted(basins, key=lambda b: len(b), reverse=True)
  return np.prod([len(basin) for basin in basins[:3]])


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
