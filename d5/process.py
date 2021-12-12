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


def getIDs(data):
  return [int(bPass.translate(str.maketrans("FLBR", "0011")), 2)
          for bPass in data]


@utils.timeit
def process(data):
  return max(getIDs(data))


@utils.timeit
def process2(data):
  seatIDs = sorted(getIDs(data))
  for index, id in enumerate(seatIDs):
    if seatIDs[index + 1] - id == 2:
      return id + 1
  return None


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  # print(process2(readData(file)))
