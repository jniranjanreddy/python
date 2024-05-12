import numpy as np

# Create a 1D array
# arr = np.array([1, 2, 3, 4, 5])

# print(arr)
# print(type(arr))
# print(arr.dtype)
# print("No. of Dimensions", arr.ndim)

# # Create a 2D array
arr = np.array([[1,2,3],[6,7,8]])
print(arr)
print("No. of Dimensions", arr.ndim)
print("")
print("-----------------Create a 3D array----------------")


# Create a 3D array
arr_3d = np.array([[[1,2,3],[6,7,8],[9,10,11]]])
print(arr_3d)
print("No. of Dimensions", arr_3d.ndim)

print("")
print("-----------------Asking user to create array----------------")
# Asking user to create array..
l = []
for i in range(1,5):
    int_1 = int(input("Enter the number of elements: "))
    l.append(int_1)
print(np.array(l))










