import os
import boto3

from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

AWS_BUCKET_NAME = str(os.getenv("AWS_BUCKET_NAME"))
AWS_ACCESS_KEY_ID = str(os.getenv("AWS_ACCESS_KEY_ID"))
AWS_SECRET_ACCESS_KEY = str(os.getenv("AWS_SECRET_ACCESS_KEY"))

s3 = boto3.client(
    "s3",
    aws_access_key_id="YOUR_ACCESS_KEY_ID",
    aws_secret_access_key="YOUR_SECRET_ACCESS_KEY",
)


def upload_file(source, destination):
    try:
        r = s3.upload_file(source, AWS_BUCKET_NAME, destination)
    except ClientError as e:
        return False
    return "https://s3.us-east-2.amazonaws.com/{}/{}".format(
        AWS_BUCKET_NAME, destination
    )
