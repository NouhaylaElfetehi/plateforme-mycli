import boto3
from botocore.exceptions import ClientError
from mycli.config import Config
from minio import Minio


class S3Service:
    def __init__(self):
        config = Config.load_config()
        self.s3 = boto3.client(
            's3',
            endpoint_url=config['s3']['endpoint_url'],
            aws_access_key_id=config['s3']['access_key'],
            aws_secret_access_key=config['s3']['secret_key']
        )
        
        self.ss3 = boto3.resource(
            's3',
            endpoint_url=config['s3']['endpoint_url'],
            aws_access_key_id=config['s3']['access_key'],
            aws_secret_access_key=config['s3']['secret_key']
        )




    def list_buckets(self):
        try:
            response = self.s3.list_buckets()
            return [bucket['Name'] for bucket in response['Buckets']]
        except ClientError as e:
            return f"Erreur: {e}"

    def create_bucket(self, bucket_name):
        try:
            self.s3.create_bucket(Bucket=bucket_name)
        except ClientError as e:
            return f"Erreur: {e}"

    def delete_bucket(self, bucket_name):
        try:
            self.s3.delete_bucket(Bucket=bucket_name)
        except ClientError as e:
            return f"Erreur: {e}"

    def upload_file(self, bucket_name, file_path):
        try:
            file_name = file_path.split("\\")[-1]
            self.s3.upload_file(file_path, bucket_name, file_name)
            # self.ss3.meta.client.upload_file(file_path, bucket_name, file_name)
        except ClientError as e:
            return f"Erreur: {e}"
    def download_file(self, bucket_name, object_name, file_path):
        try:
            self.ss3.Bucket(bucket_name).download_file( object_name, file_path)
            print(f"Fichier {object_name} téléchargé dans {file_path}.")
        except ClientError as e:
            return f"Erreur: {e}"

    def delete_file(self, bucket_name, object_name):
        try:
            self.s3.delete_object(Bucket=bucket_name, Key=object_name)
        except ClientError as e:
            return f"Erreur: {e}"
    def list_files(self, bucket_name):
        """Lister les fichiers dans un bucket."""
        try:
            response = self.s3.list_objects_v2(Bucket=bucket_name)
            if 'Contents' in response:
                return [obj['Key'] for obj in response['Contents']]
            else:
                return []
        except ClientError as e:
            return f"Erreur: {e}"

