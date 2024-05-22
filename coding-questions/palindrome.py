def palinDrome(a):
    if a == a[::-1]:
        print("Hey Its Palindron: ", a)
    else: 
        print("Its not Palindrone:", a)
        b = a[::-1]
        print(b)


palinDrome("Rama")