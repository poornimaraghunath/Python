import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask          #from flask package import the flask module

#creating flask app instance

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])      #decorators they are functions that performed before actual function exceution
def createJira():

    url = "https://poornimacr.atlassian.net/rest/api/3/issue"

    API_TOKEN="ATATT3xFfGF0esGjRq5zNl1NI1VRVkeqGlyJF770cg1Ae3qjjhHf0vwlgpKAzFiune5G8k3p2tdE845gK3ayZ9vj2nq8wOynYdGe4DWt-BPaCZNBXOHfvY5Hy6qdp9ez8udiK5WDRhgUfVOTw94uVqT2NbpsMeo5vSBZxeFvrEIzP4ubhOK7A5Q=C0C6943C"

    auth = HTTPBasicAuth("poornimaraghunath18@gmail.com", API_TOKEN)

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
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "MYP"
        },
        "issuetype": {
            "id": "10006"
        },
        "summary": "Main order flow broken",
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

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)