import requests
import json

api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlYmZiMGRlYy0zZTQxLTQ2Y2QtYmMyNS1kODZhNGQxMzE4OTkiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwianRpIjoiZWQ5OTkyMWEtNmZmOC00OWY2LWI0MDAtYTc2M2E1YTI4YjJhIiwiaWF0IjoxNzc3MzA0MzY1fQ.x266cd5PhN0wSocS7pAWbNO8-p1TlbeJakOTxm-YXDo"
workflow_id = "n7tXaZTayc5UpQDt"
base_url = "https://n8n.calvinjmckenzie.xyz/api/v1"

headers = {
    "X-N8N-API-KEY": api_key,
    "Content-Type": "application/json"
}

# 1. Get current workflow
response = requests.get(f"{base_url}/workflows/{workflow_id}", headers=headers)
workflow = response.json()

# 2. Strip restricted fields
allowed_fields = ["name", "nodes", "connections", "settings", "staticData", "meta", "tags"]
clean_workflow = {k: v for k, v in workflow.items() if k in allowed_fields}

# Update name for confirmation
clean_workflow["name"] = "Hermes Master: YouTube to Socials (Live Diagnostic)"

# 3. Push update
update_response = requests.put(f"{base_url}/workflows/{workflow_id}", headers=headers, data=json.dumps(clean_workflow))

if update_response.status_code == 200:
    print(f"Successfully updated workflow: {clean_workflow['name']}")
else:
    print(f"Failed to update workflow: {update_response.status_code}")
    print(update_response.text)
