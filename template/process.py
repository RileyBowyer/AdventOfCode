def readData(filename):
  with open(filename) as f:
    return [line.strip() for line in f]


def process(data):
  return data


def process2(data):
  return data


file = "test.txt"
# file = "data.txt"
print(process(readData(file)))
print(process2(readData(file)))