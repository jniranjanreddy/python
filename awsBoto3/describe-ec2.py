#!/usr/bin/env python3
import boto3
import paramiko
import re
import logging
# ec2 = boto3.client('ec2') #
# response = ec2.describe_instances()
# print(response)
ANSI_ESCAPE = re.compile(
    r"""
    \x1B  # ESC
    (?:   # 7-bit C1 Fe (except CSI)
        [@-Z\\-_]
    |     # or [ for CSI, followed by a control sequence
        \[
        [0-?]*  # Parameter bytes
        [ -/]*  # Intermediate bytes
        [@-~]   # Final byte
    )
""",
    re.VERBOSE,
)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='15.206.75.153',
                         username='ec2-user',
                         key_filename='seneca.pem') # Using file Argument
stdin, stdout, stderr = ssh.exec_command("uname -a | awk '{print $2}'")
insTanceName = stdout.read().decode().strip()
print(insTanceName)
# for line in iter(lambda: stdout.readline(2048), ""):
#                     cleaned = ANSI_ESCAPE.sub("", line.rstrip())
#                     logging.info(f"Stdout: {cleaned}")