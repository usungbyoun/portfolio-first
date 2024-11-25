from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = "portfolio-first-bucket/static"  # 정적 파일 경로 지정

class MediaStorage(S3Boto3Storage):
    location = "portfolio-first-bucket/media"  # 미디어 파일 경로 지정
    file_overwrite = False  # 파일 덮어쓰기 방지


