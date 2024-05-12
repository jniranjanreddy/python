import numpy as np

var = np.array([9,8,7,6])


# print(var[0])
# print(var[1])
# print(var[2])
# print(var[3])

# reverse indexing
# print(var[-1])
# print(var[-2])
# print(var[-3])
# print(var[-4])

# two dimensional array
# var1 = np.array([[2,7,3,11],[2,5,6,10]])
# print(var1[0]) # [2 7 3 11]
# print(var1[0]) # [2 7 3 11]

# print(var1[0][0]) # 2
# print(var1[0][1]) # 7
# print(var1[0][2]) # 3
# print(var1[0][3]) # 11

# print(var1[1][0]) # 9
# print(var1[1][1]) # 5
# print(var1[1][2]) # 6
# print(var1[1][3]) # 10
#                 [index 0,   index 1,  index 2]
var1 = np.array([[2,7,3],[2,7,6],[2,7,4]])
# print(f"Array 0: {var1[0]} 'AND' Array 0:0; {var1[0][0]}")
# print(f"Array 1: {var1[1]} 'AND' Array 0:1; {var1[1][0]}")
# print(f"Array 2: {var1[2]} 'AND' Array 0:2; {var1[2][0]}")

if var1[0][1] == var1[1][1] == var1[2][1]:
    print("Yes")
else:
    print("No")

print(var1.ndim)

