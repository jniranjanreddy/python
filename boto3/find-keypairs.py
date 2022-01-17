#!/usr/bin/env python3
import boto3

#ec2 = boto3.client('ec2')
#response = ec2.create_key_pair(KeyName='boto-key')
#print(response)
ec2 = boto3.resource('ec2')
instance = ec2.Instance('id')
print(ec2)
