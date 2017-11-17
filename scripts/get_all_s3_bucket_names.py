#!/usr/bin/env python
import json
import boto3
import logging


# Define boto3 connections/variables
S3Client = boto3.client('s3')


# Get all bucket names
def lambda_handler(event, context):
    S3Buckets = S3Client.list_buckets()
    AllBucketNames = []
    for bucket in S3Buckets['Buckets']:
        AllBucketNames.append(bucket['Name'])
    return AllBucketNames
