import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    template = f.readline().strip()
    f.readline()
    return template, dict([line.strip().split(" -> ") for line in f])


@utils.timeit
def process(data, iterations=10):
  polymer, rules = data
  pairs = {k: 0 for k in rules.keys()}

  for i in range(1, len(polymer)):
    pairs[polymer[i - 1:i + 1]] += 1

  for _ in range(iterations):
    tmp = {k: 0 for k in rules.keys()}
    for pair, value in pairs.items():
      sub = rules[pair]
      tmp[pair[0] + sub] += value
      tmp[sub + pair[1]] += value
    pairs = tmp

  chars = {char: 0 for keys in rules.keys() for char in keys}
  for pair, value in pairs.items():
    chars[pair[0]] += value
  chars[polymer[-1]] += 1
  
  elemFreq = sorted(chars.values(), reverse=True)
  return elemFreq[0] - elemFreq[-1]


@utils.timeit
def process2(data, iterations=40):
  return process(data, iterations)


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
