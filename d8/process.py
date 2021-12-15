import sys
import os
from itertools import permutations
import collections


sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


digitMap = {0: [0, 1, 2, 4, 5, 6],
            1: [2, 5],
            2: [0, 2, 3, 4, 6],
            3: [0, 2, 3, 5, 6],
            4: [1, 2, 3, 5],
            5: [0, 1, 3, 5, 6],
            6: [0, 1, 3, 4, 5, 6],
            7: [0, 2, 5],
            8: [0, 1, 2, 3, 4, 5, 6],
            9: [0, 1, 2, 3, 5, 6]}


def readData(filename):
  inputs = []
  outputs = []
  with open(filename) as f:
    for line in f:
      line = line.strip()
      line = line.split("|")
      inputs.append(line[0].split())
      outputs.append(line[1].split())
    return inputs, outputs


@utils.timeit
def process(data):
  inputs, outputs = data
  return sum(len(entry) in [2, 3, 4, 7]
             for entry in [val for entry in outputs for val in entry])


def findCombo(input):
  combs = permutations(["a", "b", "c", "d", "e", "f", "g"])
  for comb in combs:
    tmpInput = [collections.Counter(list(inp)) for inp in input]
    for combo in digitMap.values():
      valList = [comb[i] for i in combo]
      valStr = "".join(valList)
      if collections.Counter(list(valStr)) in tmpInput:
        tmpInput.remove(collections.Counter(list(valStr)))
        if not tmpInput:
          return comb


@utils.timeit
def process2(data):
  inputs, outputs = data
  sumVals = []
  for input, output in zip(inputs, outputs):
    sumVal = ""
    # Try all combos
    mapping = findCombo(input)
    for out in output:
      valList = [mapping.index(var) for var in iter(out)]
      for num, key in digitMap.items():
        if collections.Counter(key) == collections.Counter(valList):
          sumVal += str(num)
    sumVals.append(sumVal)
  return sum(int(sumVal) for sumVal in sumVals)


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  # print(process(readData(file)))
  print(process2(readData(file)))
