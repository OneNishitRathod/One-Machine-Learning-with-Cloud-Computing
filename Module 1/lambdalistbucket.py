import boto3

def list_bucket_names(event, context):
    # Create an S3 client
    s3 = boto3.client('s3')

    # List all the bucket names
    response = s3.list_buckets()
    bucket_names = [bucket['Name'] for bucket in response['Buckets']]

    print(bucket_names)

def lambda_handler(event, context):
    list_bucket_names(event, context)
