import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass

corresponding = {"[": "]", "{": "}", "(": ")", "<": ">"}


def readData(filename):
  with open(filename) as f:
    return [list(line.strip()) for line in f]


def readBrackets(line):
  opened = []
  for val in line:
    if val in corresponding.keys():
      opened.append(val)
    elif val == corresponding[opened[-1]]:
      opened.pop()
    else:
      return True, val
  return False, opened


@utils.timeit
def process(data):
  values = {")": 3, "]": 57, "}": 1197, ">": 25137}
  invalids = []
  for line in data:
    corrupt, end = readBrackets(line)
    if corrupt:
      invalids.append(end)
  return sum(values[invalid] for invalid in invalids if invalid is not None)


@utils.timeit
def process2(data):
  values = {")": 1, "]": 2, "}": 3, ">": 4}
  closer = []
  vals = []
  for line in data:
    corrupt, end = readBrackets(line)
    if not corrupt:
      close = [corresponding[open] for open in end[::-1]]
      closer.append(close)
  
  for close in closer:
    val = 0
    for entry in close:
      val = val * 5 + values[entry]
    vals.append(val)
  vals = sorted(vals)
  return vals[len(vals) // 2]


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  # print(process(readData(file)))
  print(process2(readData(file)))
