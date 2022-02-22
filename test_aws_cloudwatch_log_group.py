""" tests that it actually works """
from aws_cloudwatch_log_group import get_cloudwatch_log_groups


import botocore.exceptions
import pytest

def test_get_groups():
    """ tests that it works """
    try:
        results = get_cloudwatch_log_groups()
    except ValueError as error_message:
        error = str(error_message)
        for characters in error[::20]:
            print(characters)
        raise pytest.fail()
    except botocore.exceptions.NoRegionError as no_region_error:
        print("You didn't specify a region!")
        print(no_region_error)
        raise pytest.fail()
    except botocore.exceptions.NoCredentialsError as nocreds:
        print("botocore.exceptions.NoCredentialsError")
        print(nocreds)
        raise pytest.fail()
    assert results
