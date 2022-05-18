#!/usr/bin/env python3
# for x in range(10):
#     if x == 7:
#         print("processing is enough, break loop execution")
#         break
#     print(x)
# print("outside of Loop") 

cart = [10,20,30,40,50,600,30,40]
for item in cart:
    if item > 500:
        print("Cant process, it require insurance")
        break
    print(f"Processing item: {item}")
    