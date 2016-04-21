from __future__ import absolute_import

from django.conf import settings

from storages.backends.s3boto import S3BotoStorage

# Define bucket and folder for static files.
S3Storage = lambda: S3BotoStorage(
    bucket=settings.AWS_STORAGE_BUCKET_NAME,
    location='static')

MediaS3Storage = lambda: S3BotoStorage(
    bucket=settings.AWS_STORAGE_BUCKET_NAME,
    location='media')
