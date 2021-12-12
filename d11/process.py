import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    return [[char for char in line.strip()] for line in f]


def getSymbolP1(data, x, y):
  neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1),
                (1, 1), (-1, -1), (1, -1), (-1, 1)]
  
  occupiedCount = sum(data[x + dx][y + dy] == '#' for dx, dy in neighbours
                      if 0 <= x + dx < len(data) and 0 <= y + dy < len(data[x]))
  
  if data[x][y] == '#':
    return '#' if occupiedCount < 4 else 'L'
  elif data[x][y] == 'L':
    return '#' if occupiedCount == 0 else 'L'
  else:
    return '.'


def getSymbolP2(data, x, y):
  neighboursDirection = [(1, 0), (0, 1), (-1, 0), (0, -1),
                         (1, 1), (-1, -1), (1, -1), (-1, 1)]
  occupiedCount = 0
  for direction in neighboursDirection:
    i = 1
    while 0 <= i * direction[0] + x < len(data) and 0 <= i * direction[1] + y < len(data[0]):
      if data[i * direction[0] + x][i * direction[1] + y] != '.':
        occupiedCount += 1 if data[i * direction[0] + x][i * direction[1] + y] == '#' else 0
        break
      i += 1
  
  if data[x][y] == '#':
    return '#' if occupiedCount < 5 else 'L'
  elif data[x][y] == 'L':
    return '#' if occupiedCount == 0 else 'L'
  else:
    return '.'


@utils.timeit
def process(data):
  while True:
    tmpData = [[col for col in row] for row in data]
    for r, c in [(row, col)
                 for row in range(len(data))
                 for col in range(len(data[row]))]:
      tmpData[r][c] = getSymbolP1(data, r, c)
    if tmpData == data:
      return sum(row.count('#') for row in data)
    data = tmpData


@utils.timeit
def process2(data):
  while True:
    tmpData = [[col for col in row] for row in data]
    for r, c in [(row, col)
                 for row in range(len(data))
                 for col in range(len(data[row]))]:
      tmpData[r][c] = getSymbolP2(data, r, c)
    if tmpData == data:
      return sum(row.count('#') for row in data)
    data = tmpData


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  # print(process(readData(file)))
  print(process2(readData(file)))
