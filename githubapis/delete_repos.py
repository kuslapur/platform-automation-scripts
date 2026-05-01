import requests
from config import get_token

USERNAME = "kuslapur"

def delete_repo(repo_name, headers):
    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}"
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f"Deleted: {repo_name}")
    else:
        print(f"Failed: {repo_name} → {response.status_code} → {response.text}")


def main():
    token = get_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    with open("D:/python/repos.txt", "r") as f:
        repos = [line.strip() for line in f if line.strip()]

    for repo in repos:
        delete_repo(repo, headers)


if __name__ == "__main__":
    main()