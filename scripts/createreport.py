import requests
import csv

with open("D:/python/token.txt") as file:
    token = file.read().strip()


url = "https://api.github.com/user/repos"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

params = {
    "per_page": 100
}

repos = []
page = 1

while True:
    params["page"] = page
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print("❌ Error:", response.text)
        break

    data = response.json()

    if not data:
        break

    repos.extend(data)
    page += 1

# Create CSV report
with open("D:/python/github_repos_report.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Header
    writer.writerow([
        "Repo Name",
        "Private",
        "Language",
        "Stars",
        "Forks",
        "Created At",
        "Updated At",
        "URL"
    ])

    # Data rows
    for repo in repos:
        writer.writerow([
            repo["name"],
            repo["private"],
            repo["language"],
            repo["stargazers_count"],
            repo["forks_count"],
            repo["created_at"],
            repo["updated_at"],
            repo["html_url"]
        ])

print(f"✅ Report created: github_repos_report.csv ({len(repos)} repos)")