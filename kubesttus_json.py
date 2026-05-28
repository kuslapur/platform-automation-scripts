import subprocess
import json

result = subprocess.run(
    [
        "kubectl",
        "get",
        "pods",
        "-A",
        "-o",
        "json"
    ],
    capture_output=True,
    text=True
)

pods = json.loads(result.stdout)

for item in pods["items"]:
    print(
        item["metadata"]["namespace"],
        item["metadata"]["name"]
    )