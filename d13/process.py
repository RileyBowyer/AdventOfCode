import sys
import os
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    arrivalTime = int(f.readline())
    busIDs = f.readline().split(",")
    return arrivalTime, busIDs


@utils.timeit
def process(data):
  arrivalTime, busID = data
  busID = [int(x) for x in busID if x != "x"]
  idList = zip(busID, map(lambda x: x - (arrivalTime % x), busID))
  return np.prod(min(idList, key=lambda x: x[1]))


@utils.timeit
def process2(data):
  _, busID = data
  goalTime = [(num + 1, int(id)) for num, id in enumerate(busID) if id != "x"]
  counter = 0
  step = 1
  for num, id in goalTime:
    while (counter + num) % id != 0:
      counter += step
    step *= id
  return counter + 1


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
