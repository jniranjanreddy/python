#!/usr/bin/env python3

a = "Rama"
print("+".join(a))

n = 10
for number in range(1, n+1):
    if(number % 2 == 0):
        # print("{}".format(number))
        print(number)    

print(a.upper())
print(a.lower())


for i in range(1,20):
    print(i, end=' ')