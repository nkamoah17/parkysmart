import os
import boto3
from config import get_config

class BlobStorage:
    """
    BlobStorage class. This class will handle all the blob storage operations.
    """
    def __init__(self):
        self.config = get_config()
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=self.config.S3_ACCESS_KEY,
            aws_secret_access_key=self.config.S3_SECRET_KEY
        )

    def upload_file(self, file, file_id):
        """
        Upload a file to S3.
        """
        self.s3.upload_fileobj(file, self.config.S3_BUCKET, f'{file_id}/{file.filename}')

    def download_file(self, file_id, filename):
        """
        Download a file from S3.
        """
        file_obj = self.s3.get_object(Bucket=self.config.S3_BUCKET, Key=f'{file_id}/{filename}')
        return file_obj['Body'].read()

blob_storage = BlobStorage()

def get_blob_storage():
    """
    Returns the BlobStorage object
    """
    return blob_storage
