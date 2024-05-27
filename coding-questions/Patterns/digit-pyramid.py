# def print_shape(rows):
#     for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()
# # Example usage
# rows = 4
# print_shape(rows)

# for i in range(1,6):
#     for j in range(1,i+1):
#         # print(i, j)
#         print(j,end=" ")
#     print()

# rows = 5
# for i in range(1, rows + 1):
#     # Print leading spaces
#     for j in range(rows - i):
#         print("  ", end="")
    
#     # Print the numbers in descending order
#     for k in range(i, 0, -1):
#         print(k, end=" ")
    
#     # Move to the next line
#     print()

# for i in range(10, 1, -1):
#     print(i)

# for i in range(10, 1, -2):
#     print(i)


n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        # print(j)
        print("  ", end="")
    
    for k in range(i, 0, -1):
        print(k, end=" ")

    print()        



