import boto3
s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='examplebucket110011',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1',
    },
)
print(response)

#Put Object in S3 
response = s3.put_object(
    Body='filetoupload',
    Bucket='examplebucket110011',
    Key='objectKey',
    ServerSideEncryption='AES256',
)
print(response)

#Get Bucket Encryption
response = s3.get_bucket_encryption(
    Bucket='examplebucket110011'
)
print(response)

#By default Server Side encryption is done