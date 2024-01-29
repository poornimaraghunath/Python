# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os


url = "https://poornimacr.atlassian.net/rest/api/3/issue"

API_TOken = os.environ.get('JIRA_API_TOKEN')
auth = HTTPBasicAuth("poonimaraghunath18@gmail.com", API_TOken)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "my first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
   
    
    
    "issuetype": {
      "id": "10006"
    },
    
   
    
    "project": {
      "key": "MYP"           #id to key 
    },
    
    
    "summary": "My First Jira Ticket",
    
    
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))