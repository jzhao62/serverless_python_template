import time
import os
from lib.jira_helper import JiraHelper

DEFAULT_PROJECT = os.environ['DEFAULT_PROJECT']
API_TOKEN = os.environ['API_TOKEN']
USER_NAME = os.environ['USER_NAME']
SERVER = os.environ['SERVER']


jira = JiraHelper(USER_NAME, API_TOKEN, SERVER)

# Test Data for Creating Issue
test_data = {
    "project": DEFAULT_PROJECT,
    "summary": "test_summary" + str(time.time()),
    "description": "test_description",
    "issuetype": {"name": "Bug"}
}
jira.create_issue(test_data)
