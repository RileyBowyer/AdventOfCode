import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    return [[int(val) for val in line.strip()] for line in f]


@utils.timeit
def process(data, steps=100):
  adjacent = [[0, 1], [0, -1], [1, 0], [-1, 0],
              [1, 1], [1, -1], [-1, 1], [-1, -1]]
  numFlash = 0
  for _ in range(steps):
    flash = []
    for row, col in [(r, c)
                     for r in range(len(data))
                     for c in range(len(data[r]))]:
      data[row][col] += 1
      flash.append((row, col)) if data[row][col] > 9 else None

    for row, col in flash:
      for r, c in adjacent:
        newRow, newCol = row + r, col + c
        if 0 <= newRow <= len(data) - 1 and 0 <= newCol <= len(data[0]) - 1:
          data[newRow][newCol] += 1
          if data[newRow][newCol] > 9 and (newRow, newCol) not in flash:
            flash.append((row + r, col + c))
        
    for row, col in [(r, c)
                     for r in range(len(data))
                     for c in range(len(data[r]))]:
        if data[row][col] > 9:
          data[row][col] = 0
          numFlash += 1

  return numFlash


@utils.timeit
def process2(data):
  adjacent = [[0, 1], [0, -1], [1, 0], [-1, 0],
              [1, 1], [1, -1], [-1, 1], [-1, -1]]
  step = 1
  
  while True:
    flash = []
    for row, col in [(r, c)
                     for r in range(len(data))
                     for c in range(len(data[r]))]:
      data[row][col] += 1
      flash.append((row, col)) if data[row][col] > 9 else None

    for row, col in flash:
      for r, c in adjacent:
        newRow, newCol = row + r, col + c
        if 0 <= newRow <= len(data) - 1 and 0 <= newCol <= len(data[0]) - 1:
          data[newRow][newCol] += 1
          if data[newRow][newCol] > 9 and (newRow, newCol) not in flash:
            flash.append((row + r, col + c))
        
    for row, col in [(r, c)
                     for r in range(len(data))
                     for c in range(len(data[r]))]:
        if data[row][col] > 9:
          data[row][col] = 0

    if len(flash) == len(data) * len(data[0]):
      return step
    step += 1


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
