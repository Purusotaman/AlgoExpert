def solveSudoku(board):
  solve(0, 0, board)
  return board

def solve(r, c, board):
  cur_r = r
  cur_c = c
  
  # if it reaches the end, reset it to first col in next row
  if cur_c == len(board[0]):
    cur_c = 0
    cur_r += 1
    
    # if col is 9 and row is also end, we've reached the end of the board
    if cur_r == len(board):
      return True
  
  if board[cur_r][cur_c] == 0:
    return try_all_digits(cur_r, cur_c, board)
  
  return solve(cur_r, cur_c + 1, board)

def try_all_digits(r, c, board):  
  for digit in range(1, 10):
    if is_valid(r, c, board, digit):
      board[r][c] = digit
      if solve(r, c + 1, board):
        return True
      
  board[r][c] = 0
  return False

def is_valid(r, c, board, value):
  is_row_valid = value not in board[r]
  is_col_valid = value not in map(lambda r: r[c], board)
  
  if not is_row_valid or not is_col_valid:
    return False
  
  # to find starting of the each 3x3 sub-grid
  # r // 3 gives the remainder, * 3 gives the start of the sub-grid
  # essentially we are bucketing them
  start_row = (r // 3) * 3
  start_col = (c // 3) * 3
  
  for i in range(3):
    for j in range(3):
      row_to_check = start_row + i
      col_to_check = start_col + j
      
      if board[row_to_check][col_to_check] == value:
        return False
  
  return True
      
if __name__ == '__main__':
  board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
  ]

  print('Input Board')
  [print(row) for row in board]
  

  solveSudoku(board)

  print('Solved Board')
  [print(row) for row in board]


