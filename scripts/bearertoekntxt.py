from email import header
from urllib import response
import requests

with open("D:/python/token.txt", 'r') as f:
     token = f.read().strip()

url = "https://api.github.com/user/repos"

headers = {
    "authorization": f"Bearer {token}",
    "accept": "application/vnd.github+json"
}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        print(repo['name'])
else:
    print(f"Failed to fetch repositories: {response.status_code} - {response.text}")

