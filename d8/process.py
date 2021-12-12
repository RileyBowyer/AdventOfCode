import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    # return [line.strip().split(" ") for line in f]
    return [line.strip().split(" ") for line in f]


def searchIndex(data, findLoop=True):
  accumulator = 0
  index = 0
  visitedIndexes = set()
  
  while index < len(data):
    if index in visitedIndexes:
      return accumulator if findLoop else None
    visitedIndexes.add(index)
    
    command = data[index][0]
    if command == "acc":
      accumulator += int(data[index][1])
    elif command == "jmp":
      index += int(data[index][1])
      continue
    index += 1
  return None if findLoop else accumulator


@utils.timeit
def process(data):
  return searchIndex(data)


@utils.timeit
def process2(data):
  toCheck = [index for index, entry in enumerate(data)
             if entry[0] in ["jmp", "nop"]]
  swap = {"jmp": "nop", "nop": "jmp"}
  for check in toCheck:
    tmpData = data[:]
    tmpData[check] = (swap[tmpData[check][0]], tmpData[check][1])
    
    if (accumulator := searchIndex(tmpData, False)) is not None:
      return accumulator


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  # print(process(readData(file)))
  print(process2(readData(file)))
