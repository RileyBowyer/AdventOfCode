import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    return [int(line.strip()) for line in f]


@utils.timeit
def process(data, preamble=25):
  for index in range(preamble, len(data)):
    keySet = data[index - preamble:index]
    if data[index] not in [x1 + x2
                           for x1 in keySet
                           for x2 in keySet if x1 != x2]:
      return data[index]
  return data


@utils.timeit
def process2(data, preamble=25):
  invalidNum = process(data, preamble)
  for index in range(len(data)):
    numSum = []
    while sum(numSum) < invalidNum:
      numSum.append(data[index])
      index += 1
    
    if sum(numSum) == invalidNum:
      numSum.sort()
      return numSum[0] + numSum[-1]


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file), preamble=25))
  print(process2(readData(file), preamble=25))
