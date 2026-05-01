import requests

url = "https://api.github.com/user/repos"

headers = {
    "Authorization": "Bearer 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",
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