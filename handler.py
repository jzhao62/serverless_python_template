import json
import os

PROJECT_NAME = os.environ['DEFAULT_PROJECT']
API_TOKEN = os.environ['API_TOKEN']
USER_NAME = os.environ['USER_NAME']
SERVER = os.environ['SERVER']



def echo(event, context):
    body = json.loads(event["body"])
    query_paramaters = json.dumps(event["queryStringParameters"])
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "data": body,
            "query_paramaters": query_paramaters
        })

    }