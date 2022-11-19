#!/usr/bin/env python3

b = [10,20,30,40,255] # Bytes are immutable
l = bytes(b)
# print(type(b))
# print(type(l))
# for i in l:
#     print(i)

#Bites-array is mutable
ba = [10,20,30,40]
a = bytearray(ba)
print(type(a))
a[0] = 100   # adding 100 to array
# for i in a:
#     print(i)

print(f"print index: \'{a[1]}\'")
print(f"print index: \"{a[-1]}\"")
print(f"print index: \\\\{a[-1]}\\\\")

def f1():
    # print("Hello")
    return 10

c = f1()
print(c)