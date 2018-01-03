#!/usr/bin/env python
import boto3
import logging


# Program meta
vers = "1.0"
ProgramName = "get_account_name"

# Output logging - default WARNING. Set to INFO for full output in cloudwatch
logger = logging.getLogger()
logger.setLevel(logging.WARNING)

# Define boto3 connections/variables
IAMClient = boto3.client('iam')
paginator = IAMClient.get_paginator('list_account_aliases')


# Main function returns the name(s) for this AWS account
def lambda_handler(event, context):
    for response in paginator.paginate():
        AccountAliases = response['AccountAliases']
    if len(AccountAliases) > 1:
        AWSAccountName = str("-".join(AccountAliases))
    else:
        AWSAccountName = str("".join(AccountAliases))
    return AWSAccountName
