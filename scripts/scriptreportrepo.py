from urllib import response
import requests

with open ("D:/python/token.txt", "r") as file:
    token = file.read().strip()

username = "kuslapur"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

url = f"https://api.github.com/users/{username}/repos"  


response = requests.get(url, headers=headers)

if response.status_code == 200:
    repos = response.json()
    
    print(f"\nRepositories of user '{username}':\n")
    for repo in repos:
        print(f"Name: {repo['name']}")
else:
    print(f"Failed to fetch repositories for user '{username}'. Status code: {response.status_code}")



