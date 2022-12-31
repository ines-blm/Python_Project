#this function creates an s3 bucket with unique name.

import boto3 
import random

bucket_prefix = 'ines-bucket'

# this allow us to interact with the s3 API
s3_client = boto3.client('s3')

def create_unique_bucket_name(bucket_prefix):
    return ''.join([bucket_prefix, str(random.randrange(10, 101, 2))])

# body of the main'
if'__name__' == '__main__':
    try:

        response = s3_client.create_bucket(
            Bucket=create_unique_bucket_name(bucket_prefix),
            CreateBucketConfiguration={
                'LocationConstraint': 'us-west-1',
    },
)

        print(response)

    except Exception as error:
        print("an Error occured: ModuleNotFoundError")

