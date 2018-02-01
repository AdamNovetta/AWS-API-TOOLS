#!/usr/bin/env python
import json
import boto3
import logging


# Program meta
vers = "1.0"
program_name = "get_open_s3_object_permissions"


# Output logging - default WARNING. Set to INFO for full output in cloudwatch
logger = logging.getLogger()
logger.setLevel(logging.WARNING)


# Define boto3 connections/variables
S3Client = boto3.client('s3')
S3Object = boto3.resource('s3')


# Try to lookup ACL info on target file in bucket
def check_acl_status(target, ParentBucket):
    object_acl = ''
    object_acl = S3Object.ObjectAcl(ParentBucket, target)
    try:
        object_acl.load()
        acl_data = object_acl.grants
    except BaseException as e:
        print("Couldn't load ACL data for " + target + "\nInfo : " + e)
        acl_data = None
    return acl_data


# Cycle through items inside of S3 bucket
def check_bucket_contents(target):
    output = {}
    output[target] = {}
    AvailableResources = S3Client.list_objects(Bucket=target)
    if 'Contents' in AvailableResources:
        for item in AvailableResources['Contents']:
            # File ID/Name key
            FID = item['Key']
            ObjectsACL = check_acl_status(FID, target)
            Perm = ''
            if ObjectsACL:
                for Objects in ObjectsACL:
                    if "URI" in Objects['Grantee']:
                        if "AllUsers" in Objects['Grantee']['URI']:
                            Perm = str(Objects['Permission'])
                            output[target][FID] = {}
                            output[target][FID]['Issue'] = {}
                            output[target][FID]['Issue']['User'] = "AllUsers"
                            output[target][FID]['Issue']['Permission'] = Perm
    else:
        output = None
    return output


# Main function, returns any permissions on file open to 'everyone' user
def lambda_handler(event, context):
    bucket = event['BucketName']
    result = check_bucket_contents(bucket)
    try:
        if result[bucket]:
            return(result[bucket])
    except BaseException as e:
        return(None)
