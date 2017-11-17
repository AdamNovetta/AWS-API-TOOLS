#!/usr/bin/env python
import json
import boto3
import logging


# Program meta
vers = "1.0"
ProgramName = "lambda_function_relay"


lambda_client = boto3.client('lambda')


# Output logging - default WARNING. Set to INFO for full output in cloudwatch
logger = logging.getLogger()
logger.setLevel(logging.WARNING)


class call_lambda:


    lc = boto3.client('lambda')


    # Defines Lambda call that doesn't have a payload attached
    def no_input(self, function_name):
        invoke_response = call_lambda().lc.invoke(
                                            FunctionName=function_name,
                                            InvocationType='RequestResponse',
                                            )
        data = invoke_response['Payload'].read().decode()[1:-1]
        return(data)


    # Defines Lambda call that includes a payload
    def payloaded_input(self, function_name, payload):
        print("- This should be the payload: " + json.dumps(payload))
        invoke_response = call_lambda().lc.invoke(
                                            FunctionName=function_name,
                                            InvocationType='RequestResponse',
                                            Payload=payload
                                            )
        data = invoke_response['Payload'].read().decode()[1:-1]
        return(data)

def get_available_functions():
    AFList = []
    AvailableFunctions = lambda_client.list_functions()['Functions']
    for function in AvailableFunctions:
        if function['FunctionName'] != ProgramName:
            AFList.append(function['FunctionName'])
    return(AFList)


def lambda_handler(event, context):
    fn = str(event['FunctionName'])
    List = get_available_functions()
    if "FunctionPayload" in event:
        pl = event['FunctionPayload']
        print("FunctionName: \n" + fn + "\n")
        print("Payload: \n" + pl + "\n")
    else:
        print("FunctionName: \n" + fn + "\n")
    if fn in List:
        print("Function: " + fn + " is runnable!")
        try:
            if pl:
                data = call_lambda().payloaded_input(fn, pl)
        except:
                data = call_lambda().no_input(fn)
        return(data)
    else:
        print("Function: " + fn + " does not exsit or is not runnable...")
        return("Unable to run " + fn)
