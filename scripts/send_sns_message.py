#!/usr/bin/env python
import boto3
import logging


# Program meta
vers = "1.0"
program_name = "send_sns_message"


# Output logging - default WARNING. Set to INFO for full output in cloudwatch
logger = logging.getLogger()
logger.setLevel(logging.WARNING)


# Define boto3 connections/variables
SNSClient = boto3.client('sns')


# Main function send out SNS message to a given topic, provided the message/sub
def lambda_handler(event, context):
    SNSARN = event['SNSARN']
    SNSMessage = event['SNSMessage']
    SNSSubject = event['SNSSubject']
    SNSClient.publish(TopicArn=SNSARN, Message=SNSMessage, Subject=SNSSubject)
