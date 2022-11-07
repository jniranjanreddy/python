def deco_for_add(func):
    def inner(a,b):
        if b == 0:
            print("Zero cant be divided, please use non-zero")
        else:
            func(a,b)
    return inner

@deco_for_add
def add(a,b):
    print(a/b)

add(2,0)