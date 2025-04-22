# Author: Meredith Moore
# Description: Pull from DynamoDB + send via SNS

import boto3
import random

# Set up DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Lab16Jokes')

# Scan the table and select a random joke
response = table.scan()
items = response['Items']
random_joke = random.choice(items)['joke']

# Set up SNS client
sns = boto3.client('sns')
topic_arn = 'arn:aws:sns:us-east-2:REPLACE_WITH_YOUR_TOPIC_ARN' # ← Replace with your SNS topic ARN

if 'XXXXXXX' in topic_arn:
    raise ValueError("Please replace the topic_arn with your own SNS Topic ARN before running the script.")


# Send the joke via SNS
response = sns.publish(
    TopicArn=topic_arn,
    Message=random_joke,
    Subject='Joke of the Day'
)

print("Joke sent via SNS!")
