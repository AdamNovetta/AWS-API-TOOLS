#!/usr/bin/env python
import boto3
import logging


# Program meta
vers = "1.0"
ProgramName = "get_ec2_instance_name"


# Output logging - default WARNING. Set to INFO for full output in cloudwatch
logger = logging.getLogger()
logger.setLevel(logging.WARNING)


# Main function returns the EC2 instance name given an instance ID
def lambda_handler(event, context):
    InstanceName = ''
    UnNamedLabel = "no name?"
    region = event['Region']
    ec2 = boto3.resource('ec2', region_name=region)
    EC2Instance = ec2.Instance(event['EC2ID'])
    if EC2Instance.tags is not None:
        for tags in EC2Instance.tags:
            if tags["Key"] == 'Name':
                InstanceName = tags["Value"]
    else:
        InstanceName = UnNamedLabel
    return(InstanceName)
