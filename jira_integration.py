from atlassian import Jira

jira = Jira(
    url='https://alekseiivanovqa.atlassian.net',
    username='aleksei.ivanov.qa@gmail.com',
    password="ATATT3xFfGF0Gs_kuJyAO2fDd7qIHHFP7PyoRSonNVZhfS9kfWGFi-LzWiSesmuJpFIAkpnaRVmDpc7_ipSaR13YIf8PghlTPZWQVxggaJpE1TYfOQLEDUyo-WpHaOlZvGlbOWeUhUk9OYmwOLLjwWCxUrfEC5HQVeCrCGRDpot19cLxTbquDD0=63CE545A"
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