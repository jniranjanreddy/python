import boto3
import warnings
warnings.filterwarnings("ignore")
# Create IAM client
def createIAMUser(name):
    iam = boto3.client('iam', endpoint_url="http://localhost:4566")
    response = iam.create_user(UserName=name)
    print(response)

if __name__ == "__main__":
    createIAMUser("test03")