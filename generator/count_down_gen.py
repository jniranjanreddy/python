import time
def countDownGen(num):
    while num>=1:
        yield num
        num = num-1


g = countDownGen(10)
for x in g:
    print(x)
    time.sleep(1)