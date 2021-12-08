import utils
import importlib

import d1.process as d1
import d2.process as d2
import d3.process as d3
import d4.process as d4
import d5.process as d5
import d6.process as d6
import d7.process as d7


def run(day, file="test.txt"):
  g = globals()
  print("-" * 20 + f" Day {day} " + "-" * 20)
  
  # Load Data
  filePath = f"d{day}/" + file
  data = g[f"d{day}"].readData(filePath)

  # Solve Problem One
  p1Sol = g[f"d{day}"].process(data)
  print(f"Day {day}, Problem 1: {p1Sol}")
  
  # Solve Problem Two
  p2Sol = g[f"d{day}"].process2(data)
  print(f"Day {day}, Problem 2: {p2Sol}\n")


if __name__ == "__main__":
  for day in range(1, 8):
    run(day)
