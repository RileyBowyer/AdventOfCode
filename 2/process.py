def readData(filename):
  with open(filename) as f:
    return [line.strip().split(" ") for line in f]


def findPosition(commands):
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


def findPosition2(commands):
  horizontal = 0
  vertical = 0
  aim = 0
  for command in commands:
    if command[0][0] == "f":
      horizontal += int(command[1])
      vertical += aim*int(command[1])
    elif command[0][0] == "d":
      aim -= int(command[1])
    elif command[0][0] == "u":
      aim += int(command[1])
  return abs(vertical * horizontal)


print(findPosition(readData("data.txt")))
print(findPosition2(readData("data.txt")))