import boto3

session = boto3.Session()

creds = session.get_credentials()

print("Access Key:", creds.access_key)
print("Method:", creds.method)