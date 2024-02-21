# This code sample uses the 'requests' library:
# http://docs.python-requests.org

import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://poornimacr.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0esGjRq5zNl1NI1VRVkeqGlyJF770cg1Ae3qjjhHf0vwlgpKAzFiune5G8k3p2tdE845gK3ayZ9vj2nq8wOynYdGe4DWt-BPaCZNBXOHfvY5Hy6qdp9ez8udiK5WDRhgUfVOTw94uVqT2NbpsMeo5vSBZxeFvrEIzP4ubhOK7A5Q=C0C6943C"

auth = HTTPBasicAuth("poornimaraghunath18@gmail.com",API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))) {this is given entire information about the project so to only get the names use the below format}

output = json.loads(response.text)       # in python when  we need to phrase  the json data we need to convert that to dictionary json.loads is used to convert the data to dictionary)



# name1 = output[0]["name"]
# name2 = output[1]["name"]
# print(name1,name2)

names = []

for item in output :
    if 'name' in item:
        names.append(item['name'])
    else:
        names.append(None)
 
for name in names:
    print(name)