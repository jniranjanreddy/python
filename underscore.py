# for _ in range(9):
#     print("Hello")

# for _ in range(9):
#     print("ola")

board = [' ' for _ in range(9)]
for i in board:
    print(list(i))

# Function to print the board
def print_board():
 print('-------------')
 for i in range(3):
  print('|', board[i*3], '|', board[i*3 + 1], '|', board[i*3 + 2], '|')
  print('-------------')
print_board()
