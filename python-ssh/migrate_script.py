import os
import boto3
from botocore.client import Config

# Конфигурация MiniO
MINIO_URL = 'http://minio:9000'
ACCESS_KEY = 'minio_root_user'
SECRET_KEY = 'minio_root_user'
BUCKET_NAME = 'test-bucket'
NFS_DIRECTORY = '/mnt/nfs-share'

# Подключаемся к MiniO
s3_client = boto3.client(
    's3',
    endpoint_url=MINIO_URL,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    config=Config(signature_version='s3v4')
)

# Миграция файлов в MiniO
for root, dirs, files in os.walk(NFS_DIRECTORY):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        object_name = os.path.relpath(file_path, NFS_DIRECTORY)

        s3_client.upload_file(file_path, BUCKET_NAME, object_name)
        print(f"Uploaded: {file_name} to {BUCKET_NAME}/{object_name}")
