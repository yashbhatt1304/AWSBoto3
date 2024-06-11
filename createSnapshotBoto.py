import boto3
ec2 = boto3.client('ec2')

#Creating Snapshot using create_snapshots
#It uses InstanceId as mandatory filed

response = ec2.create_snapshots(
        Description="Snapshot of EC2 instance",
        InstanceSpecification={
            'InstanceId': "i-0e32a8fe1e894fdab",
            'ExcludeBootVolume': False
        },
        TagSpecifications=[
        {
            'ResourceType': 'snapshot',
            'Tags': [
                {
                    'Key': "Team",
                    'Value': "Group A"
                },
            ]
        },
        ]
)
print(response)
    

#Creating Snapshot using create_snapshot
#It uses VolumeId as mandatory filed

response = ec2.create_snapshot(
    Description='This is my root volume snapshot.',
    VolumeId='vol-0a83e06d0331af24a',
)

print(response)

