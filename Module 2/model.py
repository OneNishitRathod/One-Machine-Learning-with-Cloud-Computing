import sagemaker

# Create a SageMaker session
sagemaker_session = sagemaker.Session()

# Set the IAM role for the SageMaker session
iam_role = sagemaker.get_execution_role()

# Define the container image for the model
image = '<Your container image>'

# Define the model's S3 location
model_data = 's3://<Your model data location>'

# Create the SageMaker model
model = sagemaker.create_model(
    model_name='<Your model name>',
    role=iam_role,
    container_defs={
        'Image': image
    },
    vpc_config={
        'Subnets': ['subnet-1', 'subnet-2'],
        'SecurityGroupIds': ['sg-1']
    }
)

# Save the model to your SageMaker account
model.save(sagemaker_session=sagemaker_session)
