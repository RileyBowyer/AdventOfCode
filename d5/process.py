import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    return [[[int(num) for num in entry.split(",")]
             for entry in line.strip().split(" -> ")] for line in f]


@utils.timeit
def process(data):
  width = max([int(entry[0]) for tup in data for entry in tup])
  height = max([int(entry[1]) for tup in data for entry in tup])
  vents = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

  for tup in data:
    delta = []
    delta.append(abs(tup[0][0] - tup[1][0]))
    delta.append(abs(tup[0][1] - tup[1][1]))
    if min(delta) != 0:
      pass
    elif delta[0] != 0:
      start = abs(min(tup[0][0], tup[1][0]))
      for i in range(delta[0] + 1):
        vents[start + i][tup[0][1]] += 1
    elif delta[1] != 0:
      start = min(tup[0][1], tup[1][1])
      for i in range(delta[1] + 1):
        vents[tup[0][0]][start + i] += 1
  # for row in list(map(list, zip(*vents))):
  #   print(row)
  numOverlaps = 0
  for row in vents:
    for entry in row:
      if entry > 1:
        numOverlaps += 1
  return numOverlaps


@utils.timeit
def process2(data):
  width = max([int(entry[0]) for tup in data for entry in tup])
  height = max([int(entry[1]) for tup in data for entry in tup])
  vents = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
  for tup in data:
    delta = []
    delta.append(tup[0][0] - tup[1][0])
    delta.append(tup[0][1] - tup[1][1])
    start = [min(tup[0][0], tup[1][0]), min(tup[0][1], tup[1][1])]
    if min([abs(entry) for entry in delta]) != 0:
      for i in range(abs(delta[0]) + 1):
        rowIndex = tup[0][0] + (i if delta[0] < 0 else -i)
        colIndex = tup[0][1] + (i if delta[1] < 0 else -i)
        vents[rowIndex][colIndex] += 1
    elif delta[0] != 0:
      start = abs(min(tup[0][0], tup[1][0]))
      for i in range(abs(delta[0]) + 1):
        vents[start + i][tup[0][1]] += 1
    elif delta[1] != 0:
      start = min(tup[0][1], tup[1][1])
      for i in range(abs(delta[1]) + 1):
        vents[tup[0][0]][start + i] += 1
  # for row in list(map(list, zip(*vents))):
  #   print(row)
  numOverlaps = 0
  for row in vents:
    for entry in row:
      if entry > 1:
        numOverlaps += 1
  return numOverlaps


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
