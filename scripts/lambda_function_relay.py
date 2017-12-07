#!/usr/bin/env python
import json
import boto3
import logging


# Program meta
vers = "1.0"
ProgramName = "lambda_function_relay"


# Define boto3 connections/variables
lambda_client = boto3.client('lambda')


# Output logging - default WARNING. Set to INFO for full output in cloudwatch
logger = logging.getLogger()
logger.setLevel(logging.WARNING)


# Class to relay a call to another AWS Lambda function
class call_lambda:

    # New Boto3 connection to lambda, seperating from the first lambda_client
    lc = boto3.client('lambda')

    # Defines Lambda call that doesn't have a payload attached
    def no_input(self, function_name):
        invoke_response = call_lambda().lc.invoke(
                                            FunctionName=function_name,
                                            InvocationType='RequestResponse',
                                            )
        data = invoke_response['Payload'].read().decode()
        return(data)

    # Defines Lambda call that includes a payload
    def payloaded_input(self, function_name, payload):
        print(">> This should be the payload: " + json.dumps(payload) + "\n")
        invoke_response = call_lambda().lc.invoke(
                                            FunctionName=function_name,
                                            InvocationType='RequestResponse',
                                            Payload=json.dumps(payload)
                                            )

        data = invoke_response['Payload'].read().decode()
        return(data)


# Gets a list of all available Lambda function names in this AWS account
def get_available_functions():
    AFList = []
    AvailableFunctions = lambda_client.list_functions()['Functions']
    for function in AvailableFunctions:
        if function['FunctionName'] != ProgramName:
            AFList.append(function['FunctionName'])
    return(AFList)


# Main function - returns the output of the relayed Lambda function, given a
# function name and optional payload
def lambda_handler(event, context):
    fn = str(event['FunctionName'])
    List = get_available_functions()

    if "FunctionPayload" in event:
        pl = event['FunctionPayload']
        print("FunctionName: \n" + fn + "\nPayload: \n" + str(pl) + "\n")

    else:
        print("[ No payload sent with function: " + fn + " ]\n")

    if fn in List:
        print("Function: " + fn + " is runnable!\n")

        if pl:
            data = call_lambda().payloaded_input(fn, pl)

        else:
            data = call_lambda().no_input(fn)

        print(">>> Output from the relayed call: " + data + "\n")
        return(json.loads(data))

    else:
        print("Function: " + fn + " does not exsit or is not runnable...\n")
        return("Unable to run " + fn)
