#!/usr/bin/env python3

# f = open("resolv.conf")
# str = f.read()


# with open("resolv.conf", "r") as f:
#     # str = f.read()
#     # print(f.read(4))

# Append to file
with open("resolv.conf", "a") as f:
    # str = f.read()
    f.write("a new line \n")

with open("resolv.conf", "r") as f:
    # str = f.read()
    print(f.read())