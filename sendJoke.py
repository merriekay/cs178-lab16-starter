# Author: Meredith Moore
# Description: A Basic SNS test

import boto3

sns = boto3.client('sns', region_name='us-east-1')
topic_arn = 'arn:aws:sns:us-east-2:REPLACE_WITH_YOUR_TOPIC_ARN' # ← Replace with your SNS topic ARN

if 'XXXXXXX' in topic_arn:
    raise ValueError("Please replace the topic_arn with your own SNS Topic ARN before running the script.")

message = "Here's your joke of the day!"

response = sns.publish(
    TopicArn=topic_arn,
    Message=message,
    Subject='Joke of the Day'
)

print("Notification sent!")
