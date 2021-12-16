import sys
import os
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  with open(filename) as f:
    hexVal = f.read().strip()
    hexNum = int(hexVal, 16)
    return f"{hexNum:0{4 * len(hexVal)}b}"


def processPacket(packet):
  ver = int(packet[:3], 2)
  tid = int(packet[3:6], 2)

  if tid == 4:
    index = 6
    val = ""
    while True:
      val += packet[index + 1:index + 5]

      if packet[index] == '0':
        break
      index += 5
    payload = int(val, 2)
    end = index + 5
  else:
    sizeDescriptor = int(packet[6], 2)
    length = int(packet[7:18], 2) if sizeDescriptor else int(packet[7:22], 2) + 22
    index = 18 if sizeDescriptor else 22
    payload = []
    while True:
      if (not sizeDescriptor and index >= length
          or sizeDescriptor and len(payload) >= length):
        break
      pPacket = processPacket(packet[index:])
      index += pPacket[3]
      payload.append(pPacket)
    end = index
  return (ver, tid, payload, end)


@utils.timeit
def process(data):
  def calcPackets(payload):
    if not isinstance(payload[2], list):
      return payload[0]
    else:
      return payload[0] + sum(calcPackets(pl) for pl in payload[2])
  
  return calcPackets(processPacket(data))


@utils.timeit
def process2(data):
  opTable = {0: sum,
             1: np.prod,
             2: min,
             3: max,
             5: lambda x: int(x[0] > x[1]),
             6: lambda x: int(x[0] < x[1]),
             7: lambda x: int(x[0] == x[1])}
  
  def calcPackets(payload):
    if not isinstance(payload[2], list):
      return payload[2]
    else:
      return opTable[payload[1]]([calcPackets(pl) for pl in payload[2]])
  
  return calcPackets(processPacket(data))


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
