import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    return [line.strip() for line in f]


@utils.timeit
def process(data):
  return data


@utils.timeit
def process2(data):
  return data


if __name__ == "__main__":
  file = "test.txt"
  # file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
