import boto3

def get_all_instances():
    ec2 = boto3.client("ec2")

    paginator = ec2.get_paginator("describe_instances")

    for page in paginator.paginate():
        for reservation in page["Reservations"]:
            for instance in reservation["Instances"]:
                print(instance["InstanceId"], instance["State"]["Name"])

if __name__ == "__main__":
    get_all_instances()