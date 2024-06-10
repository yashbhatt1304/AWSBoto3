import boto3
iam = boto3.client('iam')

#Creating User
responseUser = iam.create_user(
    UserName='Bob',
)
print(responseUser)

#Creating Group
responseGroup = iam.create_group(
    GroupName='Team-A'
)
print(responseGroup)

#Attaching Policy to Group
responsePolicy = iam.add_user_to_group(
    GroupName='Team-A',
    UserName='Bob'
)
print(responsePolicy)

#Attaching Policy to Group
response = iam.attach_group_policy(
    GroupName='Team-A',
    PolicyArn='arn:aws:iam::aws:policy/ReadOnlyAccess',
)
print(response)