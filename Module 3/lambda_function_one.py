import boto3
#Create low level clients for s3 and Transcribe
s3  = boto3.client('s3')
transcribe = boto3.client('transcribe')

def lambda_handler(event, context):
    
    #parse out the bucket & file name from the event handler
    for record in event['Records']:
        file_bucket = record['s3']['bucket']['name']
        file_name = record['s3']['object']['key']
        object_url = 'https://aiservicelab3.s3.amazonaws.com/Input/AWS-Lab-3_Transcribe_Recording.mp3'
            
        response = transcribe.start_transcription_job(
            TranscriptionJobName=file_name.replace('/','')[:10],
            LanguageCode='en-US',
            MediaFormat='mp3',
            Media={
                'MediaFileUri': object_url
            })
        
        print(response)