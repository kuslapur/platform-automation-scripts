import subprocess

try:
   result = subprocess.run(["kubectl", "get", "pods"], capture_output=True, text=True, check=True)

except subprocess.CalledProcessError as e:
    print(f"Command failed with return code {e.returncode}")
    print(f"Error output: {e.stderr}")
