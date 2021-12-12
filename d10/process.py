import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    return sorted([int(line.strip()) for line in f])


@utils.timeit
def process(data):
  data.insert(0, 0)
  data.insert(len(data), data[-1] + 3)
  
  delta = {1: 0, 2: 0, 3: 0}
  for i in range(1, len(data)):
    delta[data[i] - data[i - 1]] += 1
  return delta[1] * delta[3]


@utils.timeit
def process2(data):
  data.insert(0, 0)
  data.insert(len(data), data[-1] + 3)
  
  numCombs = {key: 0 if key != data[-1] else 1 for key in data}
  for i in range(len(data) - 2, -1, -1):
    for j in range(1, 4):
      if data[i] + j in numCombs:
        numCombs[data[i]] += numCombs[data[i] + j]
  return numCombs[0]


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
