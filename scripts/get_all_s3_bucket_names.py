#!/usr/bin/env python
import json
import boto3
import logging


# Program meta
vers = "1.0"
ProgramName = "get_all_s3_bucket_names"

# Output logging - default WARNING. Set to INFO for full output in cloudwatch
logger = logging.getLogger()
logger.setLevel(logging.WARNING)

# Define boto3 connections/variables
S3Client = boto3.client('s3')


# Get all S3 bucket names
def lambda_handler(event, context):
    S3Buckets = S3Client.list_buckets()
    AllBucketNames = []
    for bucket in S3Buckets['Buckets']:
        AllBucketNames.append(bucket['Name'])
    return AllBucketNames
