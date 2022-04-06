#!/usr/bin/env python3
import os
def myHost():
    os.system('hostname -s')
a = []
a.append(10)
a.append('niru')
a.append('labs')
a.append(10)
b = myHost()
a.append(b)

print(a)
myHost() 
