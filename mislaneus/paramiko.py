#!/usr/bin/env python3
from paramiko import SSHClient
ssh = SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.9.100',username='root',password='password',port=22)
#ssh.connect(hostname='3.92.79.119',username='ec2-user',password='paramiko123',port=22)
#ssh.connect(hostname='3.92.79.119',username='ec2-user',key_filename='/home/Automation/.ssh/id_rsa',port=22)
#stdin, stdout, stderr = ssh.exec_command('whoami')
#stdin, stdout, stderr = ssh.exec_command('uptime')
stdin, stdout, stderr = ssh.exec_command('free -m')
print("The output is: ")
print(stdout.readlines())

print("THe error is: ")
print(stderr.readlines())