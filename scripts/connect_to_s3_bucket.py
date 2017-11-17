#!/usr/bin/env python
import json
import boto3
import logging


# Define boto3 connections/variables
S3Client = boto3.client('s3')

def lambda_handler(event, context):
    target = event['BucketName']
    print(target + " THIS IS THE TARGET")
    try:
        S3Client.head_bucket(Bucket=target)
        viewable = True
    except:
        viewable = False
    print("ok so this is what we'll return: " + str(viewable))
    return viewable
