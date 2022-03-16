#!/usr/bin/env python3
import boto3
def lambda_handler(event, context):
    message = "My Custom Message"
    client = boto3.client('sns')
    response = client.publish(
        TargetArn="arn:aws:sns:us-west-2:101805901231:test-boto3",
        Message=message,
        MessageStructure='text',
        Subject='This mail is from boto3')