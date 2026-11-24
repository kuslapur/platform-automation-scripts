server_name = "eks-worker-01"
environment = "PROD"
cpu_usage = 50
memory_usage = 70
disk_usage = 85
application_status = "running"

has_alert = False

print("Server name:", server_name)
print("Environment:", environment)
print("CPU usage:", cpu_usage)
print("Memory usage:", memory_usage)
print("Disk usage:", disk_usage)
print("Application status:", application_status)

if cpu_usage > 90:
    print("ALERT: High CPU usage!")
    has_alert = True

if memory_usage > 80:
    print("ALERT: High memory usage!")
    has_alert = True
if disk_usage > 90:
    print("ALERT: High disk usage!")
    has_alert = True

if has_alert:
    print("Server health check: ALERTS PRESENT")
else:
    print("Server health check: All systems normal")


if cpu_usage > 90:
   print("critical: CPU usage is above 90%")
elif cpu_usage > 80:
   print("warning: CPU usage is above 80%")
elif cpu_usage > 70:
    print("info: CPU usage is above 70%")
else:
    print("info: CPU usage is normal")





