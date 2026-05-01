import requests
from config import get_token

def create_repo(repo_name, headers):
    url = "https://api.github.com/user/repos"

    data = {
        "name": repo_name,
        "private": False  # 👈 PUBLIC repo
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Created: {repo_name}")
    else:
        print(f"Failed: {repo_name} → {response.status_code} → {response.text}")


def main():
    token = get_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    with open("D:/python/create.txt", "r") as f:
        for line in f:
            repo_name = line.strip()
            if repo_name:
                create_repo(repo_name, headers)


if __name__ == "__main__":
    main()