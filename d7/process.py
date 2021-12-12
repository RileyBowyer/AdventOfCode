import sys
import os
import re

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  bags = {}
  with open(filename) as f:
    for line in f:
      line = re.sub(" bags?|[.]", "", line.strip())
      key, rules = line.split(" contain ")
      rules = re.findall(r"([0-9]+) (\w+ \w+)", rules)
      bags[key] = {col: num for num, col in rules}
  return bags


@utils.timeit
def process(data):
  possible = []
  for root in data:
    toCheck = [root]
    for bag in toCheck:
      if "shiny gold" in data[bag]:
        possible.append(root)
        break
      toCheck.extend(data[bag].keys())
  return len(possible)


@utils.timeit
def process2(data):
  bags = [(1, "shiny gold")]
  for quantity, bag in bags:
    bags.extend([(int(num) * quantity, col) for col, num in data[bag].items()])
  return sum(num for num, col in bags) - 1


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
