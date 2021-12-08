import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    return [line.strip().split(" ") for line in f]


@utils.timeit
def process(commands):
  horizontal = 0
  vertical = 0
  for command in commands:
    if command[0][0] == "f":
      horizontal += int(command[1])
    elif command[0][0] == "d":
      vertical -= int(command[1])
    elif command[0][0] == "u":
      vertical += int(command[1])
  return abs(vertical * horizontal)


@utils.timeit
def process2(commands):
  horizontal = 0
  vertical = 0
  aim = 0
  for command in commands:
    if command[0][0] == "f":
      horizontal += int(command[1])
      vertical += aim * int(command[1])
    elif command[0][0] == "d":
      aim -= int(command[1])
    elif command[0][0] == "u":
      aim += int(command[1])
  return abs(vertical * horizontal)


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
