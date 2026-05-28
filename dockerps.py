import subprocess

result = subprocess.run(["docker", "ps"], capture_output=True, text=True)
print(result.stdout)    
print(result.stderr)
print(result.returncode)