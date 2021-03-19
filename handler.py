import json
import os

PROJECT_NAME = os.environ['DEFAULT_PROJECT']


def get_issues(event, context):
    body = {
        "message": PROJECT_NAME,
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}
    return response
