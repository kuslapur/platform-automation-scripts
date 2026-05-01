import requests

# Read token from file
with open("D:/python/token.txt") as f:
    token = f.read().strip()

username = "kuslapur"
repo_name = "repo-from-file-token"

url = f"https://api.github.com/repos/{username}/{repo_name}"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

response = requests.delete(url, headers=headers)

if response.status_code == 204:
    print("✅ Repository deleted successfully!")
else:
    print("❌ Failed to delete repo")
    print("Status:", response.status_code)
    print("Response:", response.text)

