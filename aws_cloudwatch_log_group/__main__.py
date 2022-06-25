""" simple module thing """

from json import dumps as json_dumps
import logging
import sys

import botocore.exceptions

from . import get_cloudwatch_log_groups

def main() -> None:
    """ main func """
    log = logging.getLogger(name="aws_cloudwatch_log_group")
    try:
        results = get_cloudwatch_log_groups()
    except botocore.exceptions.NoRegionError:
        log.error("You didn't specify an AWS region! (try setting environment var: AWS_DEFAULT_REGION)")
        sys.exit(1)
    except botocore.exceptions.NoCredentialsError:
        log.error("You didn't specify AWS credentials! See https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#guide-configuration for details.")
        sys.exit(1)
    except Exception as error_message: # pylint: disable=broad-except
        log.error(error_message)
        sys.exit(1)

    for result in results:
        print(json_dumps(result, default=str))

if __name__ == "__main__":
    main()
