import utils
import importlib

# TODO: Fixup 3,4,5


def run(day, file="test.txt"):
  dayMod = importlib.import_module(f"d{day}.process")
  print("-" * 20 + f" Day {day} " + "-" * 20)
  
  # Load Data
  filePath = f"d{day}/" + file
  data = dayMod.readData(filePath)

  # Solve Problem One
  p1Sol = dayMod.process(data)
  print(f"Day {day}, Problem 1: {p1Sol}")
  
  # Solve Problem Two
  p2Sol = dayMod.process2(data)
  print(f"Day {day}, Problem 2: {p2Sol}\n")


if __name__ == "__main__":
  daysCompleted = 13
  for day in range(1, daysCompleted + 1):
    run(day, "data.txt")
