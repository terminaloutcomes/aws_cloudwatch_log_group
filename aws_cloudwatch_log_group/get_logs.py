""" simple module thing """

# from json import dumps as json_dumps
import logging
import sys
from typing import Any, List, Optional

import boto3

import botocore.exceptions
import click

from aws_cloudwatch_log_group import get_cloudwatch_log_groups

def get_logs(log_client: Any, log_name: str) -> None:
    """ get the logs and print them """
    print(log_name)

    stream_data = log_client.describe_log_streams(logGroupName=log_name)
    if "logStreams" not in stream_data:
        return
    for stream in stream_data["logStreams"]:
        print(stream)
        # example:
        # {'logStreamName': '2021/10/28/[$LATEST]591435849655489fb35ef0c971ad96fc',
        # 'creationTime': 1635462030440,
        # 'firstEventTimestamp': 1635462023087,
        # 'lastEventTimestamp': 1635462238904,
        # 'lastIngestionTime': 1635462247966,
        # 'uploadSequenceToken': '49612000655872712969953454273477131888103870874418938450',
        # 'arn': 'arn:aws:logs:us-east-1:554854520534:log-group:/aws/lambda/tenderscraper:log-stream:2021/10/28/[$LATEST]591435849655489fb35ef0c971ad96fc',
        # 'storedBytes': 0} <+- this is always 0 now
    # log_client.get_log_events(
    #     logGroupName=log_name,

    # )

@click.command()
@click.argument("log_names", nargs=-1)
def main(log_names: Optional[List[str]]=None) -> None:
    """ main func """
    client = boto3.client('logs')

    logger = logging.getLogger(name="aws_cloudwatch_log_group")
    try:
        if log_names is None:
            print("include a log name plz")
            sys.exit(1)
        account_log_groups = get_cloudwatch_log_groups()

        for log_name in log_names:
            valid_log_name = False
            for account in account_log_groups:
                if log_name in account["logGroupName"]:
                    valid_log_name = True
                    break
            if valid_log_name:
                get_logs(client, log_name)
            else:
                logger.error("Error: log group '%s' not found in account", log_name)

    except botocore.exceptions.NoRegionError:
        logger.error("You didn't specify an AWS region! (try setting environment var: AWS_DEFAULT_REGION)")
        sys.exit(1)
    except botocore.exceptions.NoCredentialsError:
        logger.error("You didn't specify AWS credentials! See https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#guide-configuration for details.")
        sys.exit(1)
    except Exception as error_message: # pylint: disable=broad-except
        logger.error(error_message)
        sys.exit(1)

    # for result in results:
    #     print(json_dumps(result, default=str))

if __name__ == "__main__":
    main()
