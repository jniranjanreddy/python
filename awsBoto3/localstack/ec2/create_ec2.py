import boto3
ec2 = boto3.client('ec2', endpoint_url="http://localhost:4566", use_ssl=False)
response = ec2.describe_instances()
print(response)
