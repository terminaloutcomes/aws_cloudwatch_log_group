""" tests that it actually works """


import botocore.exceptions
# import pytest

from aws_cloudwatch_log_group import get_cloudwatch_log_groups

def test_get_groups():
    """ tests that it works """
    failed = False
    results = None
    try:
        results = get_cloudwatch_log_groups()
    except ValueError as error_message:
        error = str(error_message)
        print("Got valueerror")
        # print(dir(error))
        print(str(error).replace("-", "🍆"))
        failed = True
    except botocore.exceptions.NoRegionError as no_region_error:
        print("You didn't specify a region!")
        print(no_region_error)
        failed = True
    except botocore.exceptions.NoCredentialsError as nocreds:
        print("botocore.exceptions.NoCredentialsError")
        print(nocreds)
        failed = True
    print(f"{failed=}")
    assert results
