#!/usr/bin/env python3
import subprocess
# myHost = subprocess.check_output('hostname', shell=False,universal_newlines=True)
# myHost1 = myHost.split('/n')
cmd='hostname'
# process = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, universal_newlines=True)
process = subprocess.run(cmd,check=True,stdout=subprocess.PIPE)
output = process.stdout
print(output)
# l = []
# l.append(output)
# print(l)