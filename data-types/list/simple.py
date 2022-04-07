#!/usr/bin/env python3
import os
import subprocess

# def myHost():
#     os.system('hostname -s')
#     return;
hostname = 'hostname'
sp=subprocess.Popen(hostname,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
# print(f'OUTPUT IS: {out}')
# print(f'Error is: {err}')
l = []
l.append(10)
l.append('niru')
l.append(out)
print(out)
print(l)