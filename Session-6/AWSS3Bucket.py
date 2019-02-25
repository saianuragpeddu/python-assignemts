import boto3
# Creating S3 Client
s3 = boto3.client('s3')
# Call for S3 to list current Buckets
response = s3.list_buckets()
# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]
# Print the bucket list
print("Bucket List: %s" % buckets)

# creating a S3 Bucket name aws-pythonic-22
import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket = 'aws-pythonic-22')

# Creating a file in the bucket 'aws-pythonic-22'
import boto3

s3 = boto3.client('s3')
filename = 'SAPeddu.txt'
bucket_name = 'aws-pythonic-22'
s3.upload_file(filename, bucket_name, filename)

# Dowloading the file that is created
import boto3
import botocore

bucket_name = 'aws-pythonic-22'
key = 'SAPeddu.txt'

s3 = boto3.resource('s3')

try:
    s3.Bucket(bucket_name).download_file(key, 'download.txt') # Named as download.txt
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print('The Object does not exist.')
    else:
        raise

# creating another S3 Bucket name aws-pythonic-dup-122
import boto3

s3 = boto3.client('s3')
s3.create_bucket(Bucket = 'aws-pythonic-dup-122')


# Moving file from aws-pythonic-22 to aws-pythonic-dup-122
import boto3
s3 = boto3.resource('s3')

copy_source = {
'Bucket': 'aws-pythonic-22',
'Key': 'SAPeddu.txt'
}

bucket = s3.Bucket('aws-pythonic-dup-122')
bucket.copy(copy_source, 'MSAPeddu.txt')
