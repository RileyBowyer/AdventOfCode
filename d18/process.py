import sys
import os
import numpy as np
from copy import deepcopy

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def parseSnail(data):
  openCount = 0
  lastSplit = 0
  for index, char in enumerate(data):
    if char == '[':
      openCount += 1
    elif char == ']':
      openCount -= 1
    elif char == "," and openCount == 1:
      lastSplit = index
    
    if openCount == 0:
      firstEntry = data[1:lastSplit]
      secondEntry = data[lastSplit + 1:-1]
      if firstEntry.isnumeric():
        firstEntry = int(firstEntry)
      else:
        firstEntry = parseSnail(firstEntry)
      
      if secondEntry.isnumeric():
        secondEntry = int(secondEntry)
      else:
        secondEntry = parseSnail(secondEntry)
      return [firstEntry, secondEntry]


def readData(filename):
  with open(filename) as f:
    for line in f:
      yield parseSnail(line.strip())


def setVal(val, index, entry):
  if isinstance(entry[index], list):
    setVal(val, index, entry[index])
  else:
    entry[index] += val


def explodeSnailFish(entry, depth=0):
  # Check Explode
  depth += 1
  first, second = entry
  
  if isinstance(first, list):
    explode = explodeSnailFish(first, depth)
    if explode != (None, None):
      if explode[1] is not None:
        if isinstance(entry[1], list):
          setVal(explode[1], 0, entry[1])
        else:
          setVal(explode[1], 1, entry)
      if None not in explode:
        entry[0] = 0
      return explode[0], None

  if isinstance(second, list):
    explode = explodeSnailFish(second, depth)
    if explode != (None, None):
      if explode[0] is not None:
        if isinstance(entry[0], list):
          setVal(explode[0], 1, entry[0])
        else:
          setVal(explode[0], 0, entry)
      if None not in explode:
        entry[1] = 0
      return None, explode[1]
  
  if depth > 4:
    return entry
  else:
    return None, None


def splitSnailFish(entry):
  first, second = entry
  if isinstance(first, int):
    if first > 9:
      entry[0] = [int(np.floor(first / 2)), int(np.ceil(first / 2))]
      return True
  else:
    if splitSnailFish(first):
      return True
  if isinstance(second, int):
    if second > 9:
      entry[1] = [int(np.floor(second / 2)), int(np.ceil(second / 2))]
      return True
  else:
    if splitSnailFish(second):
      return True
  
  return False


@utils.timeit
def process(data):
  num = None
  for entry in data:
    if num is None:
      num = entry
    else:
      num = [num, entry]
    while True:
      tmp = deepcopy(num)
      explodeSnailFish(tmp)
      if tmp != num:
        num = tmp
        continue
      splitSnailFish(tmp)
      if tmp != num:
        num = tmp
        continue
      break
    print(num)
  return


@utils.timeit
def process2(data):
  return data


if __name__ == "__main__":
  file = "test.txt"
  # file = "data.txt"
  print(process(readData(file)))
  # print(process2(readData(file)))
