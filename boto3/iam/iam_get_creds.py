#!/usr/bin/env python3
import boto3

# Create IAM client
iam = boto3.client('iam')

# List access keys through the pagination interface.
paginator = iam.get_paginator('list_access_keys')
for response in paginator.paginate(UserName='nodejs'):
    print(response)