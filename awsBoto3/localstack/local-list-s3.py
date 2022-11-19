import boto3
ACCESS_KEY='123'
SECRET_KEY='abc'
s3 = boto3.client('s3',
                      endpoint_url="http://localhost:4566",
                      use_ssl=False,
                      aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
# print(s3.list_buckets())
response = s3.list_buckets()
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')