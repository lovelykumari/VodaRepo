import boto3


def getBucketName():
    s3 = boto3.resource('s3')    
    return s3.buckets.all()

def deleteBucketObjects(bktName):
    s3 = boto3.resource('s3')
    s3.Bucket(bktName).objects.delete()

def deleteBucket(bktName):
    s3 = boto3.resource('s3')
    s3.Bucket(bktName).delete()
    

for i in getBucketName():
    if 'lovely' in i.name:
       print(i.name)
       deleteBucketObjects(i.name)
       deleteBucket(i.name)