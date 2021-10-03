#!/usr/bin/env python
import os
#myHosts = { "192.168.9.103", "192.168.9.102", "192.168.9.101" } # Tuple
#myHosts = ( "192.168.9.103", "192.168.9.102", "192.168.9.101" ) # Tuple
myHosts = [ "192.168.9.103", "192.168.9.102", "192.168.9.101"] # List
for i in myHosts: 
    CMD = ("echo ${}".format(i))
    os.system(CMD)