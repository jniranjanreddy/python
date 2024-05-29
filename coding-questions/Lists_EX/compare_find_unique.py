a = [1, 2, 3, 4, 5, 6,7,8,9]

b = [1, 2, 4, 5, 6, 7,10]

# print(set(a) - set(b)) # sets can be subtracted from each other
# uniQue = list(set(a) - set(b)) # This is the same as the line below

uniQue = list(set(a).difference(b))
print(uniQue) # [8, 9, 3] 3 is the missing number.





