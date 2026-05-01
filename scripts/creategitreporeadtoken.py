import requests

with open ("D:/python/token.txt", "r") as file:
    token = file.read().strip()


url = "https://api.github.com/user/repos"

# Headers
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

# Repo data
data = {
    "name": "repo-from-file-token",
    "description": "Created using token.txt",
    "private": False
}

# API call
response = requests.post(url, json=data, headers=headers)

# Output
if response.status_code == 201:
    print("✅ Repo created:", response.json()["html_url"])
else:
    print("❌ Error:", response.status_code)
    print(response.text)