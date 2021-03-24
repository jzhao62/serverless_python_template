import json
import os

from lib.jira_helper import JiraHelper

PROJECT_NAME = os.environ['DEFAULT_PROJECT']
API_TOKEN = os.environ['API_TOKEN']
USER_NAME = os.environ['USER_NAME']
SERVER = os.environ['SERVER']

jira_helper = JiraHelper(USER_NAME, API_TOKEN, SERVER)


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

    return response


def get_project_name(event, context):
    body = {
        "message": PROJECT_NAME,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}
    return response


def get_issue_by_key(event, context):
    issue_key = event["queryStringParameters"]["issue_key"]

    issue = jira_helper.get_issue(issue_key)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "key": issue.key,
            "summary": issue.fields.summary,
            "description": issue.fields.description,
            "links": len(issue.fields.issuelinks)
        })
    }


def get_related_issues(event, context):
    issue_key = event["queryStringParameters"]["issue_key"]
    issues = jira_helper.get_related_issues(issue_key)
    ret = [];
    for issue in issues:
        ret.append({
            "key":issue.key,
            "summary": issue.fields.summary,
            "description": issue.fields.description,
            "links": len(issue.fields.issuelinks)
        })
    return {
        "statusCode": 200,
        "body": json.dumps({
            "data": ret
        })
    }
