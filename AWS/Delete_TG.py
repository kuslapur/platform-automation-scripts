import boto3

elbv2 = boto3.client('elbv2', region_name='us-east-1')

target_group_name = "hdfc-tg-01"

try:
    # Get Target Group ARN
    response = elbv2.describe_target_groups(
        Names=[target_group_name]
    )

    tg_arn = response['TargetGroups'][0]['TargetGroupArn']

    print(f"Deleting Target Group: {target_group_name}")
    print(f"ARN: {tg_arn}")

    # Delete Target Group
    elbv2.delete_target_group(
        TargetGroupArn=tg_arn
    )

    print("Target Group deleted successfully.")

except Exception as e:
    print(f"Error: {e}")