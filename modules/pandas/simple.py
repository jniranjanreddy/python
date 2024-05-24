import pandas as pd
import numpy as np

labels = ["a", "b", "c", "d", "e"]
myData = [10, 20, 30, 40]
arr = np.array(myData)
arr = np.array(labels)
myDict = {"a":10,"b":20, "c":30, "d":""}

# print("Labels", labels)
# print("myData", myData)
# print("Dictionary",myDict)
# print("Array", arr)

# print(pd.Series(data=myData))

# print(pd.Series(data=myData, index=labels))
# print(pd.Series(myData, labels))
print(pd.Series(myDict))