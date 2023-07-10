import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Call EC2 to list all running instances
response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

# Get a list of all running instances IDs from the response
instances = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]

# Print out the instance ID list
print("Running Instance ID List: %s" % instances)
