import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

# Get all running instances
response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)

instance_ids = []

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])

if instance_ids:
    print(f"Terminating instances: {instance_ids}")

    ec2.terminate_instances(
        InstanceIds=instance_ids
    )

    print("Termination initiated.")
else:
    print("No running instances found.")