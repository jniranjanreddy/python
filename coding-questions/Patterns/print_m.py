n = 10
o = 5

for i in range(1, o + 1):
    for j in range(1, i+1):
        print(j, end=" ")
    for k in range(i, n-i):
        print(" ", end=" ")
    for l in range(i, 0, -1):
        print(l, end=" ")
    print()
    
