# def print_diamond(rows):
#     # Upper half of the diamond
#     for i in range(1, rows + 1):
#         print(i)
#         print(" " * (rows - i)  + "*" * (2 * i - 1))

#     # for i in range(rows - 1, 0, -1):
#     #     print(" " * (rows - i) + "*" * (2 * i - 1))

# # rows = 5
# # print_diamond(rows)
# for i in range(1, 5 + 1):
#     print(i)

## Method 2 for Pyramids.
n = int(input("Enter the number of rows: "))
# for i in range(n):
#     print(" " * (n - i - 1) + "* " * (i + 1))

# for i in range(n):
#     print(" " * (i + 1) + "* " * (n - i - 1))

# Create a Square box
for i in range(n):
    print(" * " * n)

# Create a Hollow Square box
