import boto3
import os
import warnings
warnings.filterwarnings("ignore")
import awsBoto3.localstack.listS3Func as S3
#export PYTHONWARNINGS="ignore" # Execuet in shell command prompt to ignore warnings..

if "LOCALSTACK" in os.environ:
    print("Hey! Localstack: Execution..")
    # os.system('awslocal iam list-users')
    S3.s3_count()
else:
    print("AWS-Cloud: Execution..")
    os.system('aws iam list-users')
