import boto3
# s3=boto3.client('s3')
# res=s3.list_buckets()
# allBuckets = res['Buckets']

# for i in allBuckets:
#     print(i['Name'])

# ec2.terminate_instances(InstanceIds=[instance['InstanceId'] for item in res['Reservations'] for instance in item['Instances']])

ec2=boto3.client('ec2')
res=ec2.describe_instances()
for reservation in res['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}, Instance Type: {instance['InstanceType']}")


# for reservation in res['Reservations']:
#     for instance in reservation['Instances']:
#         # print(f"Instance ID: {instance['InstanceId']}, Instance Type: {instance['InstanceType']}")
#         if instance['State']['Name'] == 'running':
#             print(instance['InstanceId'], instance['InstanceType'], instance['State']['Name'])
#         # ec2.terminate_instances(InstanceIds=[instance['InstanceId']])