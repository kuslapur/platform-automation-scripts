from email import header
from urllib import response
import requests

username = "kuslapur"

url = f"https://api.github.com/users/{username}/repos"

#read token from file

with open("D:/python/token.txt", "r") as file:
    token = file.read().strip()


headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

response = requests.get(url, headers=headers)
repos = response.json()

for repo in repos:
    print(repo["name"])




   