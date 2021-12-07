def readData(filename):
  with open(filename) as f:
    return [[int(bit) for bit in line.strip()] for line in f]


def process(data):
  gammaRate = ""
  for index in range(len(data[0])):
    ones = 0
    zeros = 0
    for entry in data:
      if entry[index]:
        ones += 1
      else:
        zeros += 1
    if ones > zeros:
      gammaRate += "1"
    else:
      gammaRate += "0"
  gr = int(gammaRate, 2)
  er = int(gammaRate, 2)^int("1"*len(data[0]), 2)
  return gr*er

def process2(data):
  gammaRate = ""
  indicies = [i for i in range(len(data))]
  for index in range(len(data[0])):
    ones = 0
    zeros = 0
    tmp1 = []
    tmp0 = []
    if len(indicies) == 1:
      break
    for i in indicies:
      entry = data[i]
      if entry[index]:
        ones += 1
        tmp1.append(i)
      else:
        zeros += 1
        tmp0.append(i)
    if ones >= zeros:
      indicies = tmp1
    else:
      indicies = tmp0
  gammaRate = "".join([str(i) for i in data[indicies[0]]])
  gr = int(gammaRate, 2)
  
  gammaRate = ""
  indicies = [i for i in range(len(data))]
  for index in range(len(data[0])):
    ones = 0
    zeros = 0
    tmp1 = []
    tmp0 = []
    if len(indicies) == 1:
      break
    for i in indicies:
      entry = data[i]
      if entry[index]:
        ones += 1
        tmp1.append(i)
      else:
        zeros += 1
        tmp0.append(i)
    if zeros <= ones:
      indicies = tmp0
    else:
      indicies = tmp1
  gammaRate = "".join([str(i) for i in data[indicies[0]]])
  er = int(gammaRate, 2)
  
  return gr*er


print(process(readData("data.txt")))
print(process2(readData("data.txt")))