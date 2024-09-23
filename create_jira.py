import csv
from jira import JIRA
from secrets import api_token,jira_server

# Jira server connection details
project_key = 'AUTS'


# Initialize Jira client
jira_options = {'server': jira_server}
jira = JIRA(options=jira_options,token_auth=api_token )


# Function to create issues
def create_issue(summary, description, assignee, labels):
    issue_dict = {
        'project': {'key': project_key},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Task'},  # Change this to the appropriate issue type
        'assignee': {'name': assignee},
        'labels': labels.split(',') if labels else []
    }
    new_issue = jira.create_issue(fields=issue_dict)
    print(f"Issue {new_issue.key} created.")



# CSV file path
csv_file_path = 'issues.csv'


# Read CSV and create issues
with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        summary = row['summary']
        description = row['description']
        assignee = row['assignee']
        labels = row['labels']
        create_issue(summary, description, assignee, labels)