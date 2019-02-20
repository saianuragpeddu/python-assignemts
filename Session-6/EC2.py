# To find the path on which we are working
import os
cwd = os.getcwd()
print('###cwd###', cwd)
filename = os.path.join(cwd, 'ec2-launch')
# Create the Ec2 instances
import boto3
ec2 = boto3.resource('ec2', region_name = 'us-east-1')

instances = ec2.create_instances(
    ImageId='ami-035be7bafff33b6b6',
    MinCount=1,
    MaxCount=2,
    InstanceType='t2.micro',
    KeyName='ec2-launch'
)
