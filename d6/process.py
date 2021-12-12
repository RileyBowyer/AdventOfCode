import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    return [[{ans for ans in person} for line in group.split("\n")
             for person in line.split("\n")]
            for group in f.read().split("\n\n")]


@utils.timeit
def process(data):
  return sum(len(set.union(*group)) for group in data)


@utils.timeit
def process2(data):
  return sum(len(set.intersection(*group)) for group in data)


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
