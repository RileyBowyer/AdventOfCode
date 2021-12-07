def readData(filename):
  with open(filename) as f:
    return [int(line) for line in f]


def process(measures):
  increments = 0
  for i in range(1,len(measures)):
    if measures[i] > measures[i-1]:
      increments += 1
  return increments


def process2(measures):
  increments = 0
  for i in range(1,len(measures)):
    if len(measures[i:i+3]) != 3:
      continue
    if sum(measures[i:i+3]) > sum(measures[i-1:i+2]):
      increments += 1
  return increments


# file = "test.txt"
file = "data.txt"
print(process(readData(file)))
print(process2(readData(file)))