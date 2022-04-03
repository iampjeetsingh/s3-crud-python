import boto3
from botocore.exceptions import ClientError
import os
import logging

AWS_REGION = os.environ['AWS_REGION']
AWS_PROFILE = os.environ['AWS_PROFILE']
ENDPOINT_URL = os.environ['ENDPOINT_URL']

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')

boto3.setup_default_session(profile_name=AWS_PROFILE)


s3_client = boto3.client("s3", region_name=AWS_REGION, endpoint_url=ENDPOINT_URL)


def upload_file(file_name, bucket, key=None):
    """
    Upload a file to a S3 bucket.
    """
    try:
        response = s3_client.upload_file(file_name, bucket, key)
    except ClientError:
        logger.exception('Could not upload file to S3 bucket.')
        raise
    else:
        return response


def download_file(file_name, bucket, key=None):
    """
    Download a file from a S3 bucket.
    """
    try:
        response = s3_client.download_file(bucket, key, file_name)
    except ClientError:
        logger.exception('Could not download file to S3 bucket.')
        raise
    else:
        return response


def delete_file(bucket, key):
    """
    Delete a file from a s3 bucket
    """
    try:
        response = s3_client.delete_object(Bucket=bucket, Key=key)
    except ClientError:
        logger.exception('Could not download file to S3 bucket.')
        raise
    else:
        return response
