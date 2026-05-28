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

    name = item["metadata"]["name"]
    namespace = item["metadata"]["namespace"]
    phase = item["status"]["phase"]

    if phase != "Running":
        print(
            f"ALERT: {namespace}/{name} is {phase}"
        )