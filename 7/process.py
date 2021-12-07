from statistics import median, mean
def readData(filename):
  with open(filename) as f:
    return [int(num) for line in f for num in line.strip().split(",")]


def process(data):
  goal = median(data)
  return sum([abs(val - goal) for val in data])


def process2(data):
  fuel = []
  for goal in range(max(data)):
    fuel.append(sum([(abs(val - goal)**2 + abs(val - goal))/2 for val in data]))
  return min(fuel)

# file = "test.txt"
file = "data.txt"
print(process(readData(file)))
print(process2(readData(file)))