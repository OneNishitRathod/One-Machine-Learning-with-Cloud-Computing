import sagemaker

# Create a SageMaker session
sagemaker_session = sagemaker.Session()

# Set the IAM role for the SageMaker session
iam_role = sagemaker.get_execution_role()

# Define the model to deploy
model_name = '<Your model name>'

# Define the endpoint configuration
endpoint_config_name = '<Your endpoint configuration name>'
endpoint_config = sagemaker.EndpointConfig(
    endpoint_config_name=endpoint_config_name,
    production_variants=[{
        'InstanceType': 'ml.t2.medium',
        'InitialInstanceCount': 1,
        'ModelName': model_name,
        'VariantName': 'variant-1'
    }]
)

# Create the endpoint
endpoint_name = '<Your endpoint name>'
endpoint = sagemaker.Endpoint(
    endpoint_name=endpoint_name,
    sagemaker_session=sagemaker_session,
    config=endpoint_config
)

# Deploy the model to the endpoint
endpoint.deploy(initial_instance_count=1, instance_type='ml.t2.medium')
