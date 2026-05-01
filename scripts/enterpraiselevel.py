import os
import logging
import requests
from typing import List, Dict

# -----------------------------
# Configuration (Enterprise style)
# -----------------------------
GITHUB_API_URL = "https://api.github.com"
USERNAME = os.getenv("GITHUB_USERNAME", "kuslapur")
TOKEN = os.getenv("GITHUB_TOKEN")  # stored in env variable

# -----------------------------
# Logging setup
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# -----------------------------
# Headers (secure + standard)
# -----------------------------
def get_headers() -> Dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "enterprise-devops-script"
    }

    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"

    return headers


# -----------------------------
# API Call with error handling
# -----------------------------
def fetch_repositories(username: str) -> List[Dict]:
    url = f"{GITHUB_API_URL}/users/{username}/repos"

    try:
        response = requests.get(
            url,
            headers=get_headers(),
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        logging.error("Request timed out")
    except requests.exceptions.HTTPError as err:
        logging.error(f"HTTP error: {err}")
    except requests.exceptions.RequestException as err:
        logging.error(f"Request failed: {err}")

    return []


# -----------------------------
# Business Logic
# -----------------------------
def display_repositories(repos: List[Dict]) -> None:
    if not repos:
        logging.warning("No repositories found.")
        return

    logging.info(f"Found {len(repos)} repositories\n")

    for repo in repos:
        print(f"""
Name       : {repo.get('name')}
Private    : {repo.get('private')}
Language   : {repo.get('language')}
Stars      : {repo.get('stargazers_count')}
URL        : {repo.get('html_url')}
""")


# -----------------------------
# Entry Point
# -----------------------------
def main():
    logging.info(f"Fetching repositories for user: {USERNAME}")

    repos = fetch_repositories(USERNAME)
    display_repositories(repos)


if __name__ == "__main__":
    main()