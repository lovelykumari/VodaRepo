def deleteBucketObjects(bktName):
    import boto3

    AWS_REGION="us-west-1"
    S3Service=boto3.resource("s3",region_name=AWS_REGION)

    S3Service.Bucket(bktName).objects.delete()
    print("Delete Bucket: ",bktName)

bucketName="bkt19janlovely"
deleteBucketObjects(bucketName)