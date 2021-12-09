import sys


def lambda_handler(event, context):
    return 'Hello from AWS Lambda using Python and Jenkins and done some changes' + sys.version + '!'