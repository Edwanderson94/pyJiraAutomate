import os
import requests
from dotenv import load_dotenv

load_dotenv()

workspace = os.getenv("BITBUCKET_WORKSPACE")
username = os.getenv("BITBUCKET_USERNAME")
app_password = os.getenv("BITBUCKET_APP_PASSWORD")

url = f"https://api.bitbucket.org/2.0/workspaces/{workspace}"

response = requests.get(url, auth=(username, app_password))

print("Status code:", response.status_code)
print("Raw response:")
print(response.text)

if response.headers.get("Content-Type", "").startswith("application/json"):
    print("JSON response:")
    print(response.json())




print("USERNAME:", repr(username))
print("WORKSPACE:", repr(workspace))
print("TOKEN LENGTH:", len(app_password) if app_password else None)