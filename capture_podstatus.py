import subprocess

result = subprocess.run(["kubectl", "get", "pods"], capture_output=True, text=True)

print(result.stdout)
print(result.stderr)
print(result.returncode)
