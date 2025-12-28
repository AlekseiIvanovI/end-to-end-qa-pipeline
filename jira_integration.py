from atlassian import Jira
import os

from dotenv import load_dotenv

load_dotenv()

jira = Jira(
    url='https://alekseiivanovqa.atlassian.net',
    username='aleksei.ivanov.qa@gmail.com',
    password=os.getenv('JIRA_API_TOKEN')
)

def create_jira_bug(summary, description):
    issue_dict = {
        'project': {'key': 'PROJ'},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Bug'},
    }
    new_issue = jira.issue_create(fields=issue_dict)
    print(f"JIRA bug created: {new_issue['key']}")