#!/usr/bin/env python
import boto3


IAMClient = boto3.client('iam')
paginator = IAMClient.get_paginator('list_account_aliases')


def lambda_handler(event, context):
    for response in paginator.paginate():
        AccountAliases = response['AccountAliases']
    if len(AccountAliases) > 1:
        AWSAccountName = str("-".join(AccountAliases))
    else:
        AWSAccountName = str("".join(AccountAliases))
    return AWSAccountName
