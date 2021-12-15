import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
try:
  import utils
finally:
  pass


def readData(filename):
  drawOrder = []
  boards = []
  boardIndex = -1
  with open(filename) as f:
    for num, line in enumerate(f):
      if num == 0:
        drawOrder = line.split(',')
        continue
      else:
        if line.strip() == '':
          boardIndex += 1
          boards.append([])
          continue
        boards[boardIndex].append(line.strip().split())
  return drawOrder, boards


def findSol(data):
  draworder, boards = data
  for num in draworder:
    for row in range(len(boards[0][0])):
      for col in range(len(boards[0])):
        for board in boards:
          if board[row][col] == num:
            board[row][col] = 'X'
            solFound = not any(solFound and board[rowC][col] != 'X'
                               for rowC in range(len(boards[0][0])))
            if solFound:
              return num, board
            solFound = not any(solFound and board[row][colC] != 'X'
                               for colC in range(len(boards[0])))
            if solFound:
              return num, board


def findSol2(data):
  draworder, boards = data
  for num in draworder:
    for row in range(len(boards[0][0])):
      for col in range(len(boards[0])):
        for board in boards:
          if board[row][col] == num:
            board[row][col] = 'X'
            solFound = not any(solFound and board[rowC][col] != 'X'
                               for rowC in range(len(boards[0][0])))
            if solFound:
              if len(boards) == 1:
                return num, board
              boards.remove(board)
              continue
            solFound = not any(solFound and board[row][colC] != 'X'
                               for colC in range(len(boards[0])))
            if solFound:
              if len(boards) == 1:
                return num, board
              else:
                boards.remove(board)


@utils.timeit
def process(data):
  num, board = findSol(data)
  return int(num) * sum(int(x) for row in board for x in row if x != 'X')


@utils.timeit
def process2(data):
  num, board = findSol2(data)
  return int(num) * sum(int(x) for row in board for x in row if x != 'X')


if __name__ == "__main__":
  # file = "test.txt"
  file = "data.txt"
  print(process(readData(file)))
  print(process2(readData(file)))
