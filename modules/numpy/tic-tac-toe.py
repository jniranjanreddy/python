import numpy as np

# Create the tic-tac-toe board
board = np.array([['-', '-', '-'],
     ['-', '-', '-'],
     ['-', '-', '-']])

# Function to check if the game is over
def is_game_over(board):
 # Check rows
 for row in board:
  if row[0] == row[1] == row[2] != '-':
   return True

 # Check columns
 for col in board.T:
  if col[0] == col[1] == col[2] != '-':
   return True

 # Check diagonals
 if board[0, 0] == board[1, 1] == board[2, 2] != '-':
  return True
 if board[0, 2] == board[1, 1] == board[2, 0] != '-':
  return True

 # Check if the board is full
 if '-' not in board:
  return True

 return False

# Function to print the board
def print_board(board):
 for row in board:
  print(' '.join(row))

# Main game loop
while not is_game_over(board):
 print_board(board)

 # Get user input for row and column
 row = int(input("Enter the row (0-2): "))
 col = int(input("Enter the column (0-2): "))

 # Check if the chosen position is valid
 if board[row, col] == '-':
  # Update the board with the user's move
  board[row, col] = 'X'

  # Check if the game is over after the user's move
  if is_game_over(board):
   print("Game over! You win!")
   break

  # Get computer's move
  empty_positions = np.argwhere(board == '-')
  computer_move = np.random.choice(len(empty_positions))
  board[tuple(empty_positions[computer_move])] = 'O'

  # Check if the game is over after the computer's move
  if is_game_over(board):
   print("Game over! Computer wins!")
   break
 else:
  print("Invalid move. Try again.")

print_board(board)