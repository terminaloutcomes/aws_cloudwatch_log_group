""" simple module thing """

from typing import Any, Dict

import boto3


def print_groups(response: Dict[str, Any]):
    """ output """

    if response is None or "logGroups" not in response:
        return False

    for group in response["logGroups"]:
        print(group)


def main():
    """ main func """
    client = boto3.client('logs')

    response = client.describe_log_groups(
        # logGroupNamePrefix='',
        # nextToken='string',
        # limit=123
    )
    if not print_groups(response):
        return False

    while "nextToken" in response:
        response = client.describe_log_groups(nextToken=response["nextToken"])
        if not print_groups(response):
            return False

if __name__ == "__main__":
    main()
