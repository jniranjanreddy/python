#!/usr/bin/env python3
import paramiko,socket
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try: 
    #ssh.connect(hostname='192.168.9.201',username='root',password='password') # Using password Argument
    ssh.connect(hostname='192.168.9.201',
                         username='root',
                         key_filename='demo_private_key') # Using file Argument
    stdin, stdout, stderr = ssh.exec_command("uname -a | awk '{print $2}'")
    out = stdout.read().decode().strip()
    print(out)
    node_name = socket.gethostname()
    print(node_name)
    
except NameError as NM:
  print("!!Hey Something is wrong")
finally: 
    ssh.close()
