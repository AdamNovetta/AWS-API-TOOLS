#!/usr/bin/env python
import boto3
import logging


# Program meta
vers = "1.0"
program_name = "put_cloudwatch_metric"


# Output logging - default WARNING. Set to INFO for full output in cloudwatch
logger = logging.getLogger()
logger.setLevel(logging.WARNING)


# define boto3 connections
cw = boto3.client('cloudwatch')


# Main function
def lambda_handler(event, context):
    cw.put_metric_data(
        Namespace=event['Name'],
        MetricData=[{
            'MetricName': event['metricName'],
            'Value': event['value'],
            'Unit': 'Count',
            'Dimensions': [{
                'Name': 'Process',
                'Value': event['process']
                },
                {
                'Name': 'Outcome',
                'Value': event['outcome']
                }]
            }]
    )
    return(True)
