import boto3

AWS_REGION="us-west-1"
S3Service=boto3.client("s3",region_name=AWS_REGION)

location={'LocationConstraint':AWS_REGION}

response=S3Service.create_bucket(Bucket='bkt0358lovely',CreateBucketConfiguration=location)
print("Response: ",response)