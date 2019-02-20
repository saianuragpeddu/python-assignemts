import boto3
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
    ImageId='ami-04328208f4f0cf1fe',
    MinCount=1,
    MaxCount=2,
    InstanceType='t2.micro',
    KeyName='ec2-keypairpem'
)
