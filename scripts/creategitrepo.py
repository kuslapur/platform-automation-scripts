import requests

url = "https://api.github.com/user/repos"

headers = {
    "Authorization": "",
    "Accept": "application/vnd.github+json"
    }

data = {
    "name": "my-new-repo",
    "description": "Created using Python script",
    "private": False
}

response = requests.post(url, json=data, headers=headers)

print(response.status_code)
print(response.json())