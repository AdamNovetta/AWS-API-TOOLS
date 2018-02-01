#!/usr/bin/env python
import boto3
import logging


# Program meta
vers = "1.0"
program_name = "lambda_function_relay"


# Output logging - default WARNING. Set to INFO for full output in cloudwatch
logger = logging.getLogger()
logger.setLevel(logging.WARNING)


# Define boto3 connections/variables
MyAWSID = boto3.client('sts').get_caller_identity().get('Account')


# Main function returns the AWS account ID for this account
def lambda_handler(event, context):
    return(MyAWSID)
