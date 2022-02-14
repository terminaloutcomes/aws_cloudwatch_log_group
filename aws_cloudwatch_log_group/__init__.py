""" blah """

from typing import List

import boto3

def get_cloudwatch_log_groups() -> List[str]:
    """ gets the data """
    client = boto3.client('logs')

    response = client.describe_log_groups(
        # logGroupNamePrefix='',
        # nextToken='string',
        # limit=123
    )

    results: List[str] = []

    if not "logGroups" in response:
        return results
    results.extend(response["logGroups"])

    while "nextToken" in response:
        response = client.describe_log_groups(nextToken=response["nextToken"])
        if "logGroups" in response:
            results.extend(response["logGroups"])
    return results
