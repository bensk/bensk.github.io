# Create a variable board and set it equal to an empty list.

board = []

board = []

for x in range(0,5):
    board_list = ["O","O","O","O","O"]
    board.append(board_list)

print board

# Exercise 5
board = []

for x in range(0,5):
    board_list = ["O","O","O","O","O"]
    board.append(board_list)

def print_board(board):
    for row in board:
        print row

print_board(board)

# Exercise 6
board = []

for x in range(0,5):
    board_list = ["O","O","O","O","O"]
    board.append(board_list)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)
