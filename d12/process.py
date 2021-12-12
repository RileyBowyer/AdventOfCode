import sys
import os
from types import new_class
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    return [(line.strip()[0], int(line.strip()[1:])) for line in f]


def rotate(points, angle):
  newPoint = complex(points[0], points[1]) * np.exp(complex(0, np.radians(-angle)))
  return list(map(np.round, [np.real(newPoint), np.imag(newPoint)]))


@utils.timeit
def process(data):
  x = 0
  y = 0
  a = 0
  for dir, amount in data:
    if dir == "N":
      x += amount
    elif dir == "S":
      x -= amount
    elif dir == "E":
      y += amount
    elif dir == "W":
      y -= amount
    elif dir == "L":
      a += amount
    elif dir == "R":
      a -= amount
    else:
      y += amount * np.cos(np.radians(a))
      x += amount * np.sin(np.radians(a))
  return int(sum(map(abs, [x, y])))


@utils.timeit
def process2(data):
  waypoint = [1, 10]
  ship = [0, 0]
  for dir, amount in data:
    if dir == "N":
      waypoint[0] += amount
    elif dir == "S":
      waypoint[0] -= amount
    elif dir == "E":
      waypoint[1] += amount
    elif dir == "W":
      waypoint[1] -= amount
    elif dir == "L":
      waypoint = rotate(waypoint, amount)
    elif dir == "R":
      waypoint = rotate(waypoint, -amount)
    else:
      ship[0] += waypoint[0] * amount
      ship[1] += waypoint[1] * amount
  return int(sum(map(abs, ship)))


if __name__ == "__main__":
  file = "test.txt"
  file = "data.txt"
  # print(process(readData(file)))
  print(process2(readData(file)))
