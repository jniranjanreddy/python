#!/usr/bin/env python3
import boto3

ec2_resource = boto3.resource("ec2")
ec2_resource.create_instances(
    ImageId="ami-01efa4023f0f3a042", InstanceType="t2.micro", MaxCount=1, MinCount=1
)
