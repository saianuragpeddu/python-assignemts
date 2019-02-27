# Creating connection
import boto.dynamodb
conn = boto.dynamodb.connect_to_region(
    'us-east-1',
    aws_access_key_id='X',
    aws_secret_access_key='Y')

conn

# Creating Table
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    TableName= 'aws_pythonic_dynamodb',
    KeySchema=[
        {
            'AttributeName': 'Entry_ID',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'ID',
            'KeyType': 'RANGE'
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Entry_ID',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'ID',
            'AttributeType': 'N'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

# wait for table to create
table.meta.client.get_waiter('table_exists').wait(TableName= 'aws_pythonic_dynamodb')

# Print
print(table.item_count)

# Using the Created table
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('aws_pythonic_dynamodb')

print(table.creation_date_time)


# Creating Item to the Table
table.put_item(
    Item={
        'Name': 'YOUR_NNAME',
        'Entry_ID': 1,
        'ID': 101,
        'Place': 'USA'
    }
)


# Get the Item
response = table.get_item(
    Key={
        'Entry_ID': 1,
        'ID': 101
    }
)
item = response['Item']
print(item)

# Update my Name instead of YOUR_NNAME
import boto3

table = boto3.resource('dynamodb').Table('aws-pythonic-dynamodb')

table.update_item(
    Key= {'1':'101'},
    UpdateExpression="SET Name= var1",
    AttributeUpdates={
        'var1': 'SaiAnuragP',
    },
)
