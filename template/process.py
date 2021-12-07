def readData(filename):
  with open(filename) as f:
    return [line.strip() for line in f]


def process(data):
  return data


def process2(data):
  return data


print(process(readData("test.txt")))
print(process2(readData("test.txt")))