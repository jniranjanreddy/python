# Tic-Tac-Toe Game

# Create the game board
board = [' ' for _ in range(9)]
print(board)

# Function to print the game board
def print_board():
 print('-------------')
 for i in range(3):
  print('|', board[i*3], '|', board[i*3 + 1], '|', board[i*3 + 2], '|')
  print('-------------')

# Function to check if the game is over
def is_game_over():
 # Check rows
 for i in range(3):
  if board[i*3] == board[i*3 + 1] == board[i*3 + 2] != ' ':
   return True
 # Check columns
 for i in range(3):
  if board[i] == board[i + 3] == board[i + 6] != ' ':
   return True
 # Check diagonals
 if board[0] == board[4] == board[8] != ' ':
  return True
 if board[2] == board[4] == board[6] != ' ':
  return True
 return False

# Function to play the game
def play_game():
 player = 'X'
 while True:
  print_board()
  move = int(input("Enter your move (1-9): ")) - 1
  if board[move] == ' ':
   board[move] = player
   if is_game_over():
    print_board()
    print("Player", player, "wins!")
    break
   if ' ' not in board:
    print_board()
    print("It's a tie!")
    break
   player = 'O' if player == 'X' else 'X'
  else:
   print("Invalid move. Try again.")

# Start the game
play_game()