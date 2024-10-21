import os
import boto3
from botocore.client import Config

# Конфигурация MiniO
MINIO_URL = 'http://minio:9000'  # URL вашего MiniO сервера
ACCESS_KEY = 'minio_root_user'
SECRET_KEY = 'minio_root_user'
BUCKET_NAME = 'test-bucket'
NFS_DIRECTORY = '/path/to/nfs-directory'

# Подключаемся к MiniO
s3_client = boto3.client(
    's3',
    endpoint_url=MINIO_URL,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    config=Config(signature_version='s3v4')
)

# Функция для загрузки файлов на MiniO
def upload_files_to_minio(nfs_directory, bucket_name):
    for root, dirs, files in os.walk(nfs_directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            object_name = os.path.relpath(file_path, nfs_directory)

            # Загрузка файла в MiniO
            try:
                s3_client.upload_file(file_path, bucket_name, object_name)
                print(f"Successfully uploaded {file_name} to {bucket_name}/{object_name}")
            except Exception as e:
                print(f"Error uploading {file_name}: {e}")

# Создание бакета, если его нет
def create_bucket_if_not_exists(bucket_name):
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except:
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} created.")

# Запуск миграции
if __name__ == '__main__':
    create_bucket_if_not_exists(BUCKET_NAME)
    upload_files_to_minio(NFS_DIRECTORY, BUCKET_NAME)
