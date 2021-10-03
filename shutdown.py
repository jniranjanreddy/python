#!/usr/bin/env python3
myHosts = [ "192.168.9.102", "192.168.9.100"]
for i in myHosts: 
    CMD = "ssh ${} shutdown -h now".format(i)