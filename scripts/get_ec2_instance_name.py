#!/usr/bin/env python
import boto3


# Main function - returns EC2 Instance name, given a region and ID
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
