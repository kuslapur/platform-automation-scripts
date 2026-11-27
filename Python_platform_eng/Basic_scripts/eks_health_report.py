pods = {
    "frontend-01": "Running",
    "frontend-02": "Running",
    "backend-01": "CrashLoopBackOff",
    "backend-02": "Pending",
    "payment-01": "Running",
    "payment-02": "Error"
}

running = 0
failed = 0
pending = 0

for pod, status in pods.items():
    if status == "Running":
        running += 1
    elif status == "failed":
        failed += 1
    else:
        pending += 1

print("============ Health Report ============")
print()

print(f"Healthy pods: {running}")
print(f"Failed pods: {failed}")
print(f"Pending pods: {pending}")
print()

if failed > 0 or pending > 0:
    print("ALERT: Some pods are not healthy. Please check the EKS cluster for issues.")
else:
    print("All pods are healthy. EKS cluster is running smoothly.")

