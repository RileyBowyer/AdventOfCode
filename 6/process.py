def readData(filename):
  with open(filename) as f:
    return [int(num) for line in f for num in line.strip().split(",")]


def process(data, days=80):
  fishSet = [0 for _ in range(9)]
  for fish in data:
    fishSet[fish] += 1
  for _ in range(days):
    tmp = [0 for _ in range(9)]
    for i in range(9):
      tmp[i] = fishSet[(i+1)%9]
    tmp[6] = tmp[6] + fishSet[0]
    fishSet = tmp
  return sum(fishSet)


def process2(data):
  return process(data,days=256)


print(process(readData("data.txt")))
print(process2(readData("data.txt")))


# def process(initFish, days):
#   # fishSet = initFish
#   fishSet = [0 for _ in range(9)]
#   for fish in initFish:
#     fishSet[fish] = fishSet[fish] + 1
#   
      
# print(countFish([3,4,3,1,2], 256))