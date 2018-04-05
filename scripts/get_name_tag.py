#!/usr/bin/env python
import boto3
import logging


# Program meta
vers = "1.0"
program_name = "get_tag_name"


# Output logging - default WARNING. Set to INFO for full output in cloudwatch
logger = logging.getLogger()
logger.setLevel(logging.WARNING)


# Main function returns the 'Name' tag value if found in a collection of tags
def lambda_handler(event, context):
    NameTag = ''
    UnNamedLabel = "no name?"
    tags = event['Tags']
    if tags is not None:
        for tag in tags:
            if tag["Key"] == 'Name':
                NameTag = tag["Value"]
    else:
        NameTag = UnNamedLabel
    return NameTag
