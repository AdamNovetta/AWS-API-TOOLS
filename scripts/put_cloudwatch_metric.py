#!/usr/bin/env python
import boto3

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
