pods = {
    "frontend-abc": "Running",
    "frontend-xyz": "Running",
    "backend-abc": "CrashLoopBackOff",
    "payment-abc": "Pending",
    "database-abc": "Running"
}

for pod, status in pods.items():
    if status == "Running":
        print(f"{pod} is healthy")
    else:
        print(f"ALERT: {pod} is in {status} state")