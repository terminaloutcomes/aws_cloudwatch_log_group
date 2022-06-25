""" tests that it actually works """


from aws_cloudwatch_log_group import get_cloudwatch_log_groups

def test_get_groups():
    """ tests that it works """
    results = get_cloudwatch_log_groups()
    assert results
    for result in results:
        assert result.get("logGroupName")
        print(result.get("logGroupName"))

