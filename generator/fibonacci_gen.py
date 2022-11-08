def fibonacci_gen():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

g = fibonacci_gen()

# for x in g:
#     if x <=10:
#         print(x)
#     else:
#         break

count = 1
while count<=5:
    print(next(g))
    count=count+1