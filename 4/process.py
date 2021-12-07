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
            solFound = True
            for rowC in range(len(boards[0][0])):
              if solFound and board[rowC][col] != 'X':
                solFound = False
            if solFound:
              return num, board
            solFound = True
            for colC in range(len(boards[0])):
              if solFound and board[row][colC] != 'X':
                solFound = False
            if solFound:
              return num, board


def findSol2(data):
  draworder, boards = data
  for num in draworder:
    for row in range(len(boards[0][0])):
      for col in range(len(boards[0])):
        for index, board in enumerate(boards):
          if board[row][col] == num:
            board[row][col] = 'X'
            solFound = True
            for rowC in range(len(boards[0][0])):
              if solFound and board[rowC][col] != 'X':
                solFound = False
            if solFound:
              if len(boards) == 1:
                return num, board
              boards.remove(board)
              continue
            solFound = True
            for colC in range(len(boards[0])):
              if solFound and board[row][colC] != 'X':
                solFound = False
            if solFound:
              if len(boards) == 1:
                return num, board
              boards.remove(board)
              continue


def process(data):
  num, board = findSol(data)
  return int(num) * sum([int(x) for row in board for x in row if x != 'X'])


def process2(data):
  num, board = findSol2(data)
  return int(num) * sum([int(x) for row in board for x in row if x != 'X'])


# file = "test.txt"
file = "data.txt"
print(process(readData(file)))
print(process2(readData(file)))