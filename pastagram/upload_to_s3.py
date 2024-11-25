
import os
import boto3

from dotenv import load_dotenv

# .env.prod 파일 로드
load_dotenv('/home/app/web/.env.prod')

# AWS 인증 설정
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    region_name=os.environ.get('AWS_S3_REGION_NAME')
)


# 로컬 디렉토리와 S3 버킷 경로 설정
local_dir = '/home/app/web/static/'
bucket_name = os.environ.get('AWS_STORAGE_BUCKET_NAME')
s3_base_path = 'portfolio-first-bucket/static/'

# 로컬 디렉토리 내 모든 파일을 S3로 업로드
for root, dirs, files in os.walk(local_dir):
    for file in files:
        local_file = os.path.join(root, file)
        # 상대 경로를 S3 경로로 변환
        relative_path = os.path.relpath(local_file, local_dir)
        s3_key = os.path.join(s3_base_path, relative_path)

        # 파일을 S3로 업로드
        try:
            s3_client.upload_file(local_file, bucket_name, s3_key)
            print(f"Uploaded {local_file} to s3://{bucket_name}/{s3_key}")
        except Exception as e:
            print(f"Error uploading {local_file}: {e}")


# directories_to_sync = ['/home/app/web/static/', '/home/app/web/media/']
# bucket_name = os.getenv('AWS_S3_BUCKET_NAME')
# s3_base_path = 'portfolio-main-bucket/'

# # 디렉토리 내 모든 파일을 S3로 업로드
# for local_dir in directories_to_sync:
#     for root, dirs, files in os.walk(local_dir):
#         for file in files:
#             local_file = os.path.join(root, file)
#             # 상대 경로를 유지한 채로 S3 경로를 생성
#             relative_path = os.path.relpath(local_file, local_dir)
#             s3_key = os.path.join(s3_base_path, os.path.relpath(local_dir, '/home/app/web/'), relative_path)

#             # 파일을 S3로 업로드
#             try:
#                 s3_client.upload_file(local_file, bucket_name, s3_key)
#                 print(f"Uploaded {local_file} to s3://{bucket_name}/{s3_key}")
#             except Exception as e:
#                 print(f"Error uploading {local_file}: {e}")