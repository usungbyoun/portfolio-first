
import os
import boto3
from dotenv import load_dotenv

load_dotenv('/home/app/web/.env.prod')

s3_client = boto3.client(
    's3',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    region_name=os.environ.get('AWS_S3_REGION_NAME')
)

s3_resource = boto3.resource('s3')
bucket_name = os.environ.get('AWS_STORAGE_BUCKET_NAME')
bucket = s3_resource.Bucket(bucket_name)
prefix = 'portfolio-first-bucket/static/'

for obj in bucket.objects.filter(Prefix=prefix):
    try:
        s3_client.delete_object(Bucket=bucket.name,Key=obj.key)
        

    except Exception as e:
        print(f"Error delete {obj.key}: {e}")

print(f"delete: {prefix}/*")

