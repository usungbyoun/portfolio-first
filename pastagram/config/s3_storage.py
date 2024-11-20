from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = "static"  # 정적 파일 경로 지정
    custom_domain = True  # S3에서 제공하는 도메인 사용
    default_acl = 'public-read'


class MediaStorage(S3Boto3Storage):
    location = "media"  # 미디어 파일 경로 지정
    file_overwrite = False  # 파일 덮어쓰기 방지
    custom_domain = True  # S3에서 제공하는 도메인 사용
    default_acl = 'public-read'
