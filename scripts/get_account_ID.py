#!/usr/bin/env python
import boto3
import logging


# Program meta
vers = "1.0"
ProgramName = "lambda_function_relay"


# Output logging - default WARNING. Set to INFO for full output in cloudwatch
logger = logging.getLogger()
logger.setLevel(logging.WARNING)


# Define boto3 connections/variables
ec2 = boto3.resource("ec2")
EC2Client = boto3.client('ec2')
MyAWSID = boto3.client('sts').get_caller_identity().get('Account')

# Main function returns the AWS account ID for this account
def lambda_handler(event, context):
    return(MyAWSID)
