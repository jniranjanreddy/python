# a = 30
# b = 20
# c = 1
# max_num = max(a, b, c)
# min_num =  min(a, b, c)
# print(max_num)
# print(min_num)

myList = [1, 2, 5, 7, 9, 11, 13]
myList[0] = 2
myMin = min(myList)
myMax = max(myList)

print(myMin)
print(myMax)

def largestNumber(a):
    myMax = max(a)
    myMin = min(a)
    
    print("Maximum: ", myMax)
    print("Minimum: ", myMin)

largestNumber([1,3,4,10,11,11,12,13])