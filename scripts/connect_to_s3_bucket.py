#!/usr/bin/env python
import json
import boto3
import logging

# Program meta
vers = "1.0"
ProgramName = "connect_to_s3_bucket"

# Output logging - default WARNING. Set to INFO for full output in cloudwatch
logger = logging.getLogger()
logger.setLevel(logging.WARNING)

# Define boto3 connections/variables
S3Client = boto3.client('s3')

# Main function tries to connect to S3 bucket and returns True/False as result
def lambda_handler(event, context):
    target = event['BucketName']
    try:
        S3Client.head_bucket(Bucket=target)
        viewable = True
    except:
        viewable = False
    return viewable
