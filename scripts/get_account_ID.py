#!/usr/bin/env python
import boto3
def lambda_handler(event, context):
    ec2 = boto3.resource("ec2")
    EC2Client = boto3.client('ec2')
    MyAWSID = boto3.client('sts').get_caller_identity().get('Account')
    return(MyAWSID)
