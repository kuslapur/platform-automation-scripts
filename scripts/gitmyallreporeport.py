import requests
import csv

# Read token from file
with open("D:/python/token.txt") as f:
    token = f.read().strip()

url = "https://api.github.com/user/repos"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

params = {
    "per_page": 100  # max per page
}

params = {
    "per_page": 100
}

page = 1

while True:
    params["page"] = page
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print("❌ Error:", response.text)
        break

    repos = response.json()

    if not repos:
        break

    for repo in repos:
        print(repo["name"])

    page += 1