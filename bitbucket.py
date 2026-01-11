import os
import requests
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("BITBUCKET_USERNAME")
workspace = os.getenv("BITBUCKET_WORKSPACE")
token = os.getenv("BITBUCKET_APP_PASSWORD")

print("USERNAME:", repr(username))
print("WORKSPACE:", repr(workspace))
print("TOKEN LENGTH:", len(token) if token else None)

url = "https://api.bitbucket.org/2.0/user"

response = requests.get(
    url,
    auth=(username, token)
)

print("Status:", response.status_code)
print("Response:")
print(response.text)