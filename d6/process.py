import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    return [int(num) for line in f for num in line.strip().split(",")]


@utils.timeit
def process(data, days=80):
  fishSet = [0 for _ in range(9)]
  for fish in data:
    fishSet[fish] += 1
  for _ in range(days):
    tmp = [0 for _ in range(9)]
    for i in range(9):
      tmp[i] = fishSet[(i + 1) % 9]
    tmp[6] = tmp[6] + fishSet[0]
    fishSet = tmp
  return sum(fishSet)


def process2(data):
  return process(data, days=256)


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
