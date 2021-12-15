import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    return [[int(bit) for bit in line.strip()] for line in f]


@utils.timeit
def process(data):
  gammaRate = ""
  for index in range(len(data[0])):
    ones = 0
    zeros = 0
    for entry in data:
      if entry[index]:
        ones += 1
      else:
        zeros += 1
    gammaRate += "1" if ones > zeros else "0"
  gr = int(gammaRate, 2)
  er = int(gammaRate, 2) ^ int("1" * len(data[0]), 2)
  return gr * er


@utils.timeit
def process2(data):
  gammaRate = ""
  indicies = [i for i in range(len(data))]
  for index in range(len(data[0])):
    ones = 0
    zeros = 0
    tmp1 = []
    tmp0 = []
    if len(indicies) == 1:
      break
    for i in indicies:
      entry = data[i]
      if entry[index]:
        ones += 1
        tmp1.append(i)
      else:
        zeros += 1
        tmp0.append(i)
    indicies = tmp1 if ones >= zeros else tmp0
  gammaRate = "".join([str(i) for i in data[indicies[0]]])
  gr = int(gammaRate, 2)

  gammaRate = ""
  indicies = [i for i in range(len(data))]
  for index in range(len(data[0])):
    ones = 0
    zeros = 0
    tmp1 = []
    tmp0 = []
    if len(indicies) == 1:
      break
    for i in indicies:
      entry = data[i]
      if entry[index]:
        ones += 1
        tmp1.append(i)
      else:
        zeros += 1
        tmp0.append(i)
    indicies = tmp0 if zeros <= ones else tmp1
  gammaRate = "".join([str(i) for i in data[indicies[0]]])
  er = int(gammaRate, 2)

  return gr * er


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
