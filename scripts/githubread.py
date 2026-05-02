import requests

url = "https://api.github.com/user"

headers = {
    "Authorization": "",
    "Accept": "application/vnd.github+json"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)