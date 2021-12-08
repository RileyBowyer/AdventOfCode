import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    return [int(line) for line in f]


@utils.timeit
def process(measures):
  increments = 0
  for i in range(1, len(measures)):
    if measures[i] > measures[i - 1]:
      increments += 1
  return increments


@utils.timeit
def process2(measures):
  increments = 0
  for i in range(1, len(measures)):
    if len(measures[i:i + 3]) != 3:
      continue
    if sum(measures[i:i + 3]) > sum(measures[i - 1: i + 2]):
      increments += 1
  return increments


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
