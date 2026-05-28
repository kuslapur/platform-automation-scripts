# Python DevOps Automation - Day 01

## Project Overview

This project demonstrates how to use Python `subprocess` module for DevOps automation tasks.

The script executes Kubernetes commands using Python and captures command outputs programmatically.

---

# Technologies Used

* Python
* subprocess module
* Kubernetes
* kubectl

---

# Features

* Execute Kubernetes commands from Python
* Capture stdout and stderr
* Handle command failures
* Automate DevOps operations
* Parse command outputs

---

# Project Structure

```text
.
├── app.py
├── README.md
```

---

# Sample Python Code

```python
import subprocess

result = subprocess.run(
    ["kubectl", "get", "pods"],
    capture_output=True,
    text=True
)

print(result.stdout)
```

---

# Prerequisites

Install:

* Python 3.x
* kubectl
* Minikube or Kubernetes cluster

Verify Kubernetes connectivity:

```bash
kubectl get nodes
```

---

# Run Application

```bash
python app.py
```

---

# Expected Output

```text
NAME      READY   STATUS
nginx     1/1     Running
```

---

# Important subprocess Concepts

| Concept             | Description                |
| ------------------- | -------------------------- |
| subprocess.run      | Execute system commands    |
| stdout              | Standard output            |
| stderr              | Error output               |
| returncode          | Command execution status   |
| capture_output=True | Capture terminal output    |
| text=True           | Convert bytes to string    |
| check=True          | Raise exception on failure |

---

# DevOps Use Cases

This project demonstrates real-world DevOps automation concepts such as:

* Kubernetes monitoring
* Container management
* Infrastructure automation
* CI/CD scripting
* Health checking
* Auto-remediation

---

# Future Improvements

* Parse Kubernetes JSON outputs
* Detect unhealthy pods
* Restart failed deployments
* Add Slack alerts
* Integrate AI log analysis using Ollama
* Deploy using Docker and Kubernetes

---

# Learning Goals

By completing this project, you learn:

* Python subprocess automation
* Kubernetes command execution
* Error handling
* Production-style scripting
* DevOps automation fundamentals

---

# Author

Basavaraj Kuslapur

DevOps + AI Learning Challenge
