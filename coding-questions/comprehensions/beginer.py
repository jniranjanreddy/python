# Create a list of squares from 1 to 10.
# squares = [x**2 for x in range(1, 11)]
# print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#############################################
#Generate a list of even numbers from 1 to 20.
# evens = [x for x in range(1, 21) if x % 2 == 0]
# print(evens)  # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
####################################################

# Create a list of characters from the string "hello".
# a = "Hello"
# b = list(a)

# myList = [x for x in a]
# print(myList)

#######################
# // Generate a list of lengths of each word in a given sentence.
# sentence = "The quick brown fox jumps over the lazy dog"

# mynewList = []
# break_down_to_list = sentence.split()
# for i in break_down_to_list:
#     mynewList.append(len(i))
# print(break_down_to_list)
# print(mynewList)

# myList = [ len(x) for x in sentence.split()]
# print(myList)
########################
# Create a list of the first letters of each word in a given sentence.

# sentence = "The quick brown fox jumps over the lazy dog"
# # make_it_list = sentence.split()
# make_it_list = [x[0] for x in sentence.split() ]


# newList = []
# for i in make_it_list:
#     newList.append(i[0])
# print(newList)

# print(make_it_list)
##################################
# Generate a list of tuples (x, x^2) for x in the range 1 to 10.
# squares_tuples = [(x, x**2) for x in range(1, 11)]
# print(squares_tuples)  # Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]
##################################
#Flatten a 2D list into a 1D list.
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flat_list = [num for row in matrix for num in row]
# print(flat_list)

# zipped = list(zip(matrix))
# print(zipped)


# myRange = [x for x in range(5)]
# print(set(myRange))

# Generate a list of palindromic numbers between 1 and 1000.
# palindromes = [x for x in range(1, 1001) if str(x) == str(x)[::-1]]
# print(palindromes)  # Output: [1, 2, 3, ..., 999, 1001]


# # Create a list of all possible pairs from two lists.
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# pairs = [(x, y) for x in list1 for y in list2]
# print(pairs)  # Output: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]

matrix.append([10,11])
# print(matrix[2][2])
# print(matrix)

for i in matrix:
    print(*i)











