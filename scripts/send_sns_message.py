import boto3


SNSClient = boto3.client('sns')


def lambda_handler(event, context):
    SNSARN = event['SNSARN']
    SNSMessage = event['SNSMessage']
    SNSSubject = event['SNSSubject']
    SNSClient.publish(TopicArn=SNSARN, Message=SNSMessage, Subject=SNSSubject)
