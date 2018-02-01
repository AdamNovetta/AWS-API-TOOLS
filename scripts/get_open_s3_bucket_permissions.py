#!/usr/bin/env python
import json
import boto3
import logging


# Program meta
vers = "1.0"
program_name = "get_open_s3_bucket_permissions"


# Output logging - default WARNING. Set to INFO, for full output in cloudwatch
logger = logging.getLogger()
logger.setLevel(logging.WARNING)


# Define boto3 connections/variables
S3Client = boto3.client('s3')
S3Buckets = S3Client.list_buckets()
S3Object = boto3.resource('s3')


# Try to connect to S3 bucket
def connect_to_bucket(target):
    try:
        S3Client.head_bucket(Bucket=target)
        viewable = True
    except BaseException as e:
        viewable = False
    return viewable


# Get buckets ACL data
def get_bucket_acl_data(target):
    bucket_acl = S3Object.BucketAcl(target)
    ACLData = bucket_acl.grants
    return ACLData


# Audit ACL data to see if bucket has bad permissions
def audit(acldata):
    Issues = ""
    for grants in acldata:
        for grantee in grants['Grantee']:
            if "AllUsers" in grants['Grantee'][grantee]:
                Issues = "Everyone"
            if "AuthenticatedUsers" in grants['Grantee'][grantee]:
                Issues = "Any AWS user (not just your account)"
    return(Issues)


# Main function, returns any permissions on file open to 'everyone' user
def lambda_handler(event, context):
    bucket = event['BucketName']
    access = connect_to_bucket(bucket)
    if access:
        BucketACL = get_bucket_acl_data(bucket)
        result = audit(BucketACL)
        if result:
            return(result)
        else:
            return(None)
    else:
        return("Unable to view to bucket ACL data")
