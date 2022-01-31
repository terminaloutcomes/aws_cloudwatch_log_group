from aws_cloudwatch_log_group import example_function


def test_example_function():
    assert example_function() == 2
