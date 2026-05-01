import csv
import requests
from datetime import datetime
import zipfile
import os

username = "kuslapur"

url = f"https://api.github.com/users/{username}/repos"


response = requests.get(url)

repos = response.json()

filename = f"github_repo_report_{datetime.now().strftime('%Y%m%d')}.csv"
zip_filename = filename.replace(".csv", ".zip")

with open(filename, "w", newline="") as file:
  fieldnames = ["Repo Name", "Private", "Stars", "Forks", "URL"]
  writer = csv.DictWriter(file, fieldnames=fieldnames)

  writer.writeheader()

  for repo in repos:
      writer.writerow({
          "Repo Name": repo.get("name"),
           "Private": repo.get("private"),
           "Stars": repo.get("stargazers_count"),
           "Forks": repo.get("forks_count"),
           "URL": repo.get("html_url")
      })
print(f"{filename} created successfully")

with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(filename)

print(f"{zip_filename} created successfully")

# (Optional) delete original CSV
os.remove(filename)
print("Original CSV removed")


