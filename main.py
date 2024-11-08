import os
import requests
from requests.auth import HTTPBasicAuth

# Set up your credentials and base URL
JIRA_BASE_URL = "https://examplecompany.atlassian.net"
EMAIL = "your-email@example.com"
API_TOKEN = "your-api-token"
PROJECT_KEY = "YOUR_PROJECT_KEY"
TEAM_FIELD_ID = "customfield_10021"  # Replace with the actual ID for the Team field
TEAM_NAME = "Your Team Name"

JQL_QUERY = f'project = {PROJECT_KEY} AND "{TEAM_FIELD_ID}" = "{TEAM_NAME}"'  # Example query

# API endpoint
url = f"{JIRA_BASE_URL}/rest/api/3/search"

# API headers
headers = {
    "Accept": "application/json"
}

# Parameters for the request
params = {
    "jql": JQL_QUERY,
    "fields": "*all",  # Update this with your actual story points field ID
    "maxResults": 100  # Set to the maximum number of results you want
}

# Send the request
response = requests.get(
    url,
    headers=headers,
    params=params,
    auth=HTTPBasicAuth(EMAIL, API_TOKEN)
)

# Parse the response
if response.status_code == 200:
    data = response.json()
    tickets = data["issues"]
    
    # Initialize counters for story points and ticket count
    total_story_points = 0
    ticket_count = 0
    # print(tickets[0])
    # Loop through tickets and count story points
    for ticket in tickets:
        
        story_points = ticket["fields"].get("customfield_14430")  # Replace with your story points field ID
        total_story_points += story_points if story_points else 0
        ticket_count += 1
    
    print(f"Total Tickets: {ticket_count}")
    print(f"Total Story Points: {total_story_points}")
else:
    print(f"Failed to retrieve tickets. Status code: {response.status_code}")
    print(response.text)
