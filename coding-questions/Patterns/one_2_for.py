rows = 5
for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print("  ", end="")
    
    # Print the numbers in descending order
    for k in range(i, 0, -1):
        print(k, end=" ")
    
    # Move to the next line
    print()
