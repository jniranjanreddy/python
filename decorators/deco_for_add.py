def deco_for_add(func):
    def inner(a,b):
        print("#" * 10)
        print('The Sum:', end='')
        func(a,b)
        print("#" * 10)
    return inner

@deco_for_add
def add(a,b):
    print(a+b)

add(10,20)


