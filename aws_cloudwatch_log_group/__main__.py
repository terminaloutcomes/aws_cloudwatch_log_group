""" simple module thing """

from . import get_cloudwatch_log_groups

def main() -> None:
    """ main func """
    results = get_cloudwatch_log_groups()
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
