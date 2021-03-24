import time
import json
from lib.jira_helper import JiraHelper

from config.settings import USER_NAME, API_TOKEN, SERVER, DEFAULT_PROJECT

jira = JiraHelper(USER_NAME, API_TOKEN, SERVER)

# Test Data for Creating Issue
test_data = {
    "project": DEFAULT_PROJECT,
    "summary": "test_summary" + str(time.time()),
    "description": "test_description",
    "issuetype": {"name": "Bug"}
}
# jira.create_issue(test_data)


issues = jira.get_related_issues('JTP-1')
ret = [];
for issue in issues:
    ret.append({
        "summary": issue.fields.summary,
        "description": issue.fields.description,
    })

print(ret)
