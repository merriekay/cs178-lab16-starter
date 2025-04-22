# Author: Meredith Moore
# Description: Pull from DynamoDB + send via SNS

import boto3

# Replace with your actual SNS Topic ARN
topic_arn = 'arn:aws:sns:us-east-1:123456789012:JokeTopic'  # <-- Replace this!

# Create SNS client with region specified
sns = boto3.client('sns', region_name='us-east-1')  # <-- Replace with your region if different

# Your message
message = "Hello, world! This is a test message from SNS."

# Send message
response = sns.publish(
    TopicArn=topic_arn,
    Message=message,
    Subject='SNS Test'
)

print("Message sent!")

