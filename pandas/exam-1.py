#!/usr/bin/env python3
import pandas as pd

# orders = pd.read_table('http://bit.ly/chiporders')
# print(orders.tail(2))

# users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None)
# print(users)

ufo = pd.read_csv('http://bit.ly/uforeports')
print(type(ufo))