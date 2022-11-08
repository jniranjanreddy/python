#!/usr/bin/env python3
from nirulabs import myIP, f
def wish(name):
    print("Good Morning Sir: ", name)
greeting=wish
# print(id(greeting))

del wish
# print(id(wish))
greeting("Rama")

a = "Rama"
# print(" ".join(a))
b = "minikube.nirulabs.com"
c = b.split(".")
print(c)
myIP()
f() # This call decorators
