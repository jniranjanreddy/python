def gen_list(n):
    i = 1
    while i<=n:
        yield i
        i = i+1

g = gen_list(10)
l = list(g)
print(l)

my_list = [1,2,3,4,5]
for i in my_list:
    print(i)

