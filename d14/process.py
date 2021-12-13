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
    commands = []
    for line in f:
      if line.startswith("mem"):
        commands.extend(re.findall(r"mem\[(\d+)\] = (\d+)", line))
      else:
        commands.append(re.findall(r"mask = ([0-9,X]+)", line))
    return commands


def doMask(mask, value):
  preMask = ["1" if m == "X" else "0" for m in mask[0]]
  preMask = int("".join(preMask), 2)
  mask = [v if v != "X" else "0" for v in mask[0]]
  mask = int("".join(mask), 2)
  return (value & preMask) | mask


@utils.timeit
def process(data):
  commands = data
  mem = {}
  mask = None
  for command in commands:
    if len(command) == 1:
      mask = command
    else:
      mem[int(command[0])] = doMask(mask, int(command[1]))
  return sum(mem.values())


@utils.timeit
def process2(data):
  return data


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  # print(process2(readData(file)))
