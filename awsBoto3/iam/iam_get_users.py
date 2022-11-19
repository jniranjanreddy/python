#!/usr/bin/env python3
import boto3

# Create IAM client
iam = boto3.client('iam')


def list_users():
    iam = boto3.client("iam")
    paginator = iam.get_paginator('list_users')
    for response in paginator.paginate():
        for user in response["Users"]:
            # print(f"Username: {user['UserName']}, Arn: {user['Arn']}")
            print(f"{user['UserName']}")

list_users()