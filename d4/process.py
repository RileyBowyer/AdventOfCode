import sys
import os
import re

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  passports = []
  with open(filename) as f:
    pp = {}
    for line in f:
      line = line.strip()
      if line == "":
        passports.append(pp)
        pp = {}
        continue
      tmp = dict(entry.split(":") for entry in line.split(" "))
      pp.update(tmp)
    return passports


@utils.timeit
def process(data):
  requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
  return sum(int(all(key in pp.keys()
                     for key in requiredFields)) for pp in data)


@utils.timeit
def process2(data):
  requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
  validFuncs = {"byr": lambda x: 1920 <= int(x) <= 2002,
                "iyr": lambda x: 2010 <= int(x) <= 2020,
                "eyr": lambda x: 2020 <= int(x) <= 2030,
                "hgt": lambda x: ((x.endswith("cm") and 150 <= int(x[:-2]) <= 193) or 
                                  (x.endswith("in") and 59 <= int(x[:-2]) <= 76)),
                "hcl": lambda x: bool(re.match("#[0-9a-f]{6}$", x)),
                "ecl": lambda x: x in ["amb", "blu", "gry", "grn", "hzl", "oth"],
                "pid": lambda x: bool(re.match("[0-9]{9}$", x)),
                "cid": lambda x: True}
  
  return sum(int(all(validFuncs[key](pp[key]) for key in pp.keys()) and
                 all(key in pp.keys() for key in requiredFields))
             for pp in data)


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
