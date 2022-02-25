#!/usr/bin/env python3

from fabric import Connection
from fabric import SerialGroup
# connection = Connection(host = "root@192.168.9.201", connect_kwargs = {"password" : "password"})
# connection.run("hostname -i")

result = Connection('192.168.9.201').run('hostname', hide=True)
print(result)
