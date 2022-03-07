#!/usr/bin/env python3

from fabric import Connection
# from fabric import SerialGroup
c = Connection(host = "root@192.168.9.100", connect_kwargs = {"password" : "password"})
result = c.run("hostname -i")
out = 
# result = Connection('192.168.9.100').run('hostname', hide=True)
print(result)
