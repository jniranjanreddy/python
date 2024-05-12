import numpy as np

x = np.array([1,2,3,4,2,6,7,2,9,10])
y = np.where(x == 2, 1, 0)
print(y) # (array([1, 4, 7]),)