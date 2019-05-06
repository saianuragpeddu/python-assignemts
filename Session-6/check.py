import boto3

# Creating S3 Client
s3 = boto3.client('s3')

# Call for S3 to list current Buckets
response = s3.list_buckets()

# Get a list of all bucket names from the response
buckets = [bucket['Name'] for bucket in response['Buckets']]

# Print the bucket list
print("Bucket List: %s" % buckets)
