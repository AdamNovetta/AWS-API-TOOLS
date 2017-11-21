#!/usr/bin/env python
import json
import boto3
import logging
import time
import datetime
from time import mktime

# Program meta
vers = "1.0"
ProgramName = "get_IAM_user_IDs"


# output logging for INFO, to see full output in cloudwatch, default to warning
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# define boto3 connections/variables
IAM = boto3.resource('iam')
IAM_client = boto3.client('iam')


def lambda_handler(event, context):

    AllIAMUsers = IAM_client.list_users()
    userIDs = {}
    for users in AllIAMUsers['Users']:
        name = users['UserName']
        ID = users['UserId']
        userIDs[name] = ID
    return(userIDs)