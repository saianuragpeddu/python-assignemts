import boto3
ec2 = boto3.resource('ec2')

outfile = open('ec2-keypair_new.pem','w')

key_pair = ec2.create_key_pair(KeyName='ec2-kaypair_new')

keypairout = str(key_pair.key_material)
print(keypairout)
outfile.write(keypairout)

---
