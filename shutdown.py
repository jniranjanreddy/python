#!/usr/bin/env python
import os
myHosts = [ "192.168.9.103", "192.168.9.100"]
for i in myHosts: 
    print(i)
    CMD = ("ssh ${} shutdown -h now".format(i))
    os.system(CMD)
