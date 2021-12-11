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
def process(data):
  valid = [(entry1, entry2)
           for entry1 in data
           for entry2 in data if entry1 + entry2 == 2020]
  return valid[0][0] * valid[0][1]


@utils.timeit
def process2(data):
  valid = [(entry1, entry2, entry3)
           for entry1 in data
           for entry2 in data
           for entry3 in data if entry1 + entry2 + entry3 == 2020]
  return valid[0][0] * valid[0][1] * valid[0][2]


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  # print(process(readData(file)))
  print(process2(readData(file)))
