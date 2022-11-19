import boto3
count = []
def s3_count():
    s3 = boto3.client('s3', endpoint_url="http://localhost:4566", use_ssl=False,)
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        count.append(bucket["Name"])
    print("Total Buckets: ", len(count))

if __name__ == "__main__":
    s3_count()