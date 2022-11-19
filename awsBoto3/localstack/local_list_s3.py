import boto3
s3 = boto3.client('s3', endpoint_url="http://localhost:4566", use_ssl=False,)
# print(s3.list_buckets())
response = s3.list_buckets()
count = []
for bucket in response['Buckets']:
    count.append(bucket["Name"])
    # print(bucket["Name"])
print("Total Buclets: ", len(count))
