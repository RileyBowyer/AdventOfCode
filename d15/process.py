import sys
import os
import queue as Q

from queue import PriorityQueue, Queue

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    return [[int(x) for x in line.strip()] for line in f]


@utils.timeit
def process(data):
  dims = (len(data), len(data[0]))
  start = (0, 0)
  goal = (dims[0] - 1, dims[1] - 1)

  visited = set()
  lowest_weights = {}

  queue = PriorityQueue()
  queue.put((0, start))
  while not queue.empty():
    cost, pos = queue.get()
    visited.add(pos)
    
    if pos == goal:
      return cost

    x, y = pos
    for neighbor in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
      if 0 <= neighbor[0] < dims[0] and 0 <= neighbor[1] < dims[1]:
        if neighbor in visited:
          continue

        new_weight = cost + data[neighbor[0]][neighbor[1]]
        old_weight = lowest_weights.get(neighbor)
        if old_weight and new_weight >= old_weight:
          continue

        lowest_weights[neighbor] = new_weight
        queue.put((new_weight, neighbor))


@utils.timeit
def process2(data, tiles=5):
  for line in data:
    tmpLine = line[:]
    for _ in range(tiles - 1):
      tmpLine = [(x) % 9 + 1 for x in tmpLine]
      line.extend(tmpLine)

  newRows = data[:][:]
  for _ in range(tiles - 1):
    newRows = [[(x) % 9 + 1 for x in row] for row in newRows]
    data.extend(newRows)
  
  return process(data)


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
