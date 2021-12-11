import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  output = []
  with open(filename) as f:
    for line in f:
      line = line.strip().split(" ")
      valRange = [int(x) for x in line[0].split("-")]
      letter = line[1][0]
      password = line[2]
      output.append((valRange, letter, password))
  return output


@utils.timeit
def process(data):
  return sum(password.count(letter) in
             list(range(valRange[0], valRange[1] + 1))
             for valRange, letter, password in data)


@utils.timeit
def process2(data):
  return sum(int((password[valRange[0] - 1] == letter) ^
                 (password[valRange[1] - 1] == letter))
             for valRange, letter, password in data)


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  # print(process(readData(file)))
  print(process2(readData(file)))
