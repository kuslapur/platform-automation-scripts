import requests
from config import get_token

USERNAME = "kuslapur"

def rename_repo(old_name, new_name, headers):
    url = f"https://api.github.com/repos/{USERNAME}/{old_name}"
    payload = {
        "name": new_name
    }

    response = requests.patch(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"Renamed: {old_name} → {new_name}")
    else:
        print(f"Failed: {old_name} → {response.status_code} → {response.text}")


def main():
    token = get_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json"
    }

    with open("D:/python/rename.txt", "r") as f:
        for line in f:
            if not line.strip():
                continue
            old_name, new_name = line.strip().split(",")
            rename_repo(old_name, new_name, headers)


if __name__ == "__main__":
    main()