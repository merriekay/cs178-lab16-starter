# Author: Meredith Moore
# Description: A Basic SNS test

import boto3

sns = boto3.client('sns')
topic_arn = 'arn:aws:sns:us-east-2:REPLACE_WITH_YOUR_TOPIC_ARN' # ← Replace with your SNS topic ARN

message = "Here's your joke of the day!"

response = sns.publish(
    TopicArn=topic_arn,
    Message=message,
    Subject='Joke of the Day'
)

print("Notification sent!")
