import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  connections = {}
  with open(filename) as f:
    for line in f:
      c1, c2 = line.strip().split('-')
      connections[c1] = connections.get(c1, []) + [c2]
      connections[c2] = connections.get(c2, []) + [c1]
    return connections


@utils.timeit
def process(data):
  paths = []
  toCheck = [tuple(["start"])]
  visited = set()
  while toCheck:
    current = toCheck.pop()
    
    if current[-1] == "end":
      paths.append(current)
      continue
    
    for connection in data[current[-1]]:
      proposed = tuple(list(current) + [connection])
      doubleCheck = [c for c in proposed if c.islower()]
      if len(doubleCheck) != len(set(doubleCheck)):
        continue
      
      if proposed not in visited:
        toCheck.append(proposed)
        visited.add(proposed)
  return len(paths)


@utils.timeit
def process2(data):
  paths = []
  toCheck = [tuple(["start"])]
  visited = set()
  while toCheck:
    current = toCheck.pop()
    
    if current[-1] == "end":
      paths.append(current)
      continue
    
    for connection in data[current[-1]]:
      if connection == "start":
        continue

      proposed = tuple(list(current) + [connection])
      doubleCheck = [c for c in proposed if c.islower()]
      if len(doubleCheck) - len(set(doubleCheck)) > 1:
        continue
      
      if proposed not in visited:
        toCheck.append(proposed)
        visited.add(proposed)
  return len(paths)


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
