import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(instance["InstanceId"])