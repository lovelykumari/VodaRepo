import boto3

S3Service=boto3.resource("s3")

for b in S3Service.buckets.all():
    print(b.name)