#!/usr/bin/env python

f = open("/etc/hosts", "r")
for i in f:
    print(i)