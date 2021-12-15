from statistics import median, mean
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
def process(data):
  goal = median(data)
  return int(sum(abs(val - goal) for val in data))


@utils.timeit
def process2(data):
  fuel = [sum((abs(val - goal)**2 + abs(val - goal)) / 2 for val in data)
          for goal in range(max(data))]
  return int(min(fuel))


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
