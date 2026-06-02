import boto3

# Create ELBv2 client
elbv2 = boto3.client('elbv2', region_name='us-east-1')

alb_name = "hdfc-Application-LB"

try:
    # Get ALB details
    response = elbv2.describe_load_balancers(
        Names=[alb_name]
    )

    alb_arn = response['LoadBalancers'][0]['LoadBalancerArn']

    print(f"Found ALB: {alb_name}")
    print(f"ARN: {alb_arn}")

    # Delete ALB
    elbv2.delete_load_balancer(
        LoadBalancerArn=alb_arn
    )

    print("ALB deletion initiated successfully.")

except Exception as e:
    print(f"Error: {e}")