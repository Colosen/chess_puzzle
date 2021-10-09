import random

# Puzzle to place 8 queens on a chessboard without any of them cutting each other

# Creating 64 x 64 chessboard


board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],]


'''
def create_board():
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]

    for i in range(0, 65):
        for j in range(0, 65):
            board[i][j] == 0
'''
# Placing 8 queens

def place_queens():
    for i in range(0, 8):
        for j in range(0, 8):
            if is_placeable(i, j):
                board[i][j] = 1

def is_placeable(i, j):

    row_check = 0
    column_check = 0
    up_diagonal_check = 0
    row_diagonal_check = 0

    # row-check
    for a in range(0, 8):
        if board[a][j] == 1:
            row_check = 1

    # column-check
    for a in range(0, 8):
        if board[i][a] == 1:
            column_check = 1

    '''       
    # diagonal-check
    for a in range(1, 9):
    if board[i][a] == 'Q':
        column_check += 1

    # column-check
    for a in range(1, 9):
    if board[i][a] == 'Q':
        column_check += 1
    '''

    if row_check == 0 and column_check == 0:
        return True
    else:
        return False

def print_board():
    for a in range(0, 8):
        for b in range(0, 8):
            print(board[a][b], end = '')
        print()

# create_board
place_queens()
print_board()

