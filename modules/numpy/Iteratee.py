import numpy as np

var = np.array([[1,2,3,4],[9,8,7,6],[10,11,12,13]])

# for i in var:
#     print(i)

print("---------------------")

# Two dimensional for loop
# for i in var:
#     for j in i:
#         print(j)

print("---------------------")
# Three dimensional for loop
var1 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# print(var1.ndim)
# for i in var1:
#     for j in i:
#         for k in j:
#             print(k)
# for i in np.nditer(var1):
#     print(i)

# for i, j in np.ndenumerate(var1):
#     print(i,j)

# If its in Three dimensions, you can use the following to print the whole array
print(var1[0][0][0]) # [1 2 3]
print(var1[0][0][1]) # [1 2 3]
print(var1[0][0][2]) # [1 2 3]
print(var1[0][1][0]) # [4 5 6]
print(var1[0][2][0] ) # [7 8 9]

var1[0][2][0] = 12
print(var1[0][2][0] ) # [7 8 9]

