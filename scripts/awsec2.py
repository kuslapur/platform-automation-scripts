from urllib import response
import boto3
import csv

ec2 = boto3.client('ec2', region_name='ap-south-1')

response = ec2.describe_instances()

with open('ec2_instances.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['Instance ID', 'Instance Type', 'State', 'Public IP', 'Private IP', 'Launch Time'])

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            
            instance_id = instance.get('InstanceId', '')
            instance_type = instance.get('InstanceType', '')
            state = instance.get('State', {}).get('Name', '')
            private_ip = instance.get('PrivateIpAddress', '')
            public_ip = instance.get('PublicIpAddress', '')
            
            name = ''
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if tag['Key'] == 'Name':
                        name = tag['Value']

            # Write row
            writer.writerow([
                instance_id,
                instance_type,
                state,
                private_ip,
                public_ip,
                name
            ])
print("✅ EC2 report generated: ec2_report.csv")