import boto3
import json
import sagemaker
from sagemaker import image_uris

# Create a SageMaker session
sagemaker_session = sagemaker.Session()

# Specify your AWS Region
aws_region='us-east-1'

# Create a low-level SageMaker service client.
sagemaker_client = boto3.client('sagemaker', region_name=aws_region)

# Role to give SageMaker permission to access AWS services.
sagemaker_role= "arn:aws:iam::094583137742:role/LabRole"

#Create a variable w/ the model S3 URI
s3_bucket = 'moduletwosession' # Provide the name of your S3 bucket
#bucket_prefix='module'
model_s3_key = "moduletwosession/output/nr-training-job/output/model.tar.gz"

#Specify S3 bucket w/ model
model_url = "s3://moduletwosession/output/nr-training-job/output/model.tar.gz"

# Specify an AWS container image. 
container = image_uris.retrieve(region=aws_region, framework='xgboost', version='1.5-1')

model_name = 'labtwoinferedmodel'

#Create model
Model = sagemaker_client.create_model(
    ModelName = model_name,
    ExecutionRoleArn = sagemaker_role,
    PrimaryContainer={
        'Image': container,
        'ModelDataUrl': model_url,
    },
    VpcConfig={
        'SecurityGroupIds': ['sg-02a70fd403812815d'],
        'Subnets': ['subnet-0f86713d96cc602cc','subnet-0166bf1263b97bc42']
    }
)
