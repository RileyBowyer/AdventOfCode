import sys
import os
import re

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    line = f.read()
    regEx = "(([-]?[\d]+)[.]{2}([-]?[\d]+))"
    groups = re.findall(regEx, line)
    groups = [(int(group[1]), int(group[2])) for group in groups]
    return groups


def findSpeeds(ranges):
  xRange, yRange = ranges
  sols = []
  for xSpeed in range(xRange[1] + 1):
    for ySpeed in range(yRange[0], -yRange[0] + 1):
      pos = [0, 0]
      step = [xSpeed, ySpeed]
      while pos[0] <= xRange[1] and pos[1] >= yRange[0]:
        if (xRange[0] <= pos[0] <= xRange[1] and
            yRange[0] <= pos[1] <= yRange[1]):
          sols.append((xSpeed, ySpeed))
          break
        pos[0] += step[0]
        pos[1] += step[1]
        
        if step[0] != 0:
          step[0] += 1 if step[0] < 0 else -1
        step[1] -= 1
  return sols


@utils.timeit
def process(data):
  peakY = max(findSpeeds(data), key=lambda x: x[1])[1]
  return int((peakY ** 2 + peakY) / 2)


@utils.timeit
def process2(data):
  return len(findSpeeds(data))


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
