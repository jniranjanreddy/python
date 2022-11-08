import os

def first_n_values_gen(n):
    i = 1
    while i<=n:
        yield i
        i = i+1
g = first_n_values_gen(10)
for i in g:
    print(i)

    
# def gen1():
#     g = (x*x for x in range(10))
#     while True:
#         print(next(g))
#     return None

# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'

# g = mygen()
# for i in g:
#     print(i)



# if __name__=="__main__":
#     mygen()