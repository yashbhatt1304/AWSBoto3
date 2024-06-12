import boto3
ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

Groups=[]
Ids=[]
Types=[]

#############  this method returns the details for all the EC2 instances  ##############
response = ec2.describe_instances(
)

for i in response["Reservations"]:
    for j in i["Instances"]:
        Ids.append(j["InstanceId"])
        Types.append(j["InstanceType"])
        for tags in j["Tags"]:
            Groups.append(tags["Value"])

##############  get all the S3 bucket and then get tags for each bucket  #############
s3Response = s3.list_buckets()
for i in s3Response["Buckets"]:
    Ids.append(i["Name"])
    tagResponse = s3.get_bucket_tagging(
        Bucket=i["Name"]
    )
    Types.append("AmazonS3")
    for j in tagResponse["TagSet"]:
        Groups.append(j["Value"])

print(Groups)
print(Ids)
print(Types)

