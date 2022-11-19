import logging
import boto3
from botocore.exceptions import ClientError
# ACCESS_KEY='123'
# SECRET_KEY='abc'

def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """
    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3', endpoint_url="http://localhost:4566" )
            s3_client.create_bucket(Bucket=bucket_name)   # to Create Bucket
            # s3_client.delete_bucket(Bucket=bucket_name) # to Delete Bucket
        else:
            s3_client = boto3.client('s3', endpoint_url="http://localhost:4566", region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True
if __name__ == "__main__":
    create_bucket("test03")