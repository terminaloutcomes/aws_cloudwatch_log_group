""" blah """

from typing import Any, Dict, List

try:
    from mypy_boto3_logs.type_defs import LogGroupTypeDef
except ImportError:
    class LogGroupTypeDefDict(Dict[Any,Any]):
        """ overload for when you're in prod but don't have the stubs """

import boto3

def get_cloudwatch_log_groups() -> List[LogGroupTypeDef]:
    """ gets the data """
    client = boto3.client('logs')

    response = client.describe_log_groups(
        # logGroupNamePrefix='',
        # nextToken='string',
        # limit=123
    )

    results: List[LogGroupTypeDef] = []

    if not "logGroups" in response:
        return results
    results.extend(response["logGroups"])

    while "nextToken" in response:
        response = client.describe_log_groups(nextToken=response["nextToken"])
        if "logGroups" in response:
            results.extend(response["logGroups"])
    return results
