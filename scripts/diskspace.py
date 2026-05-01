import psutil
import time

CPU_THRESHOLD = 80
MEM_THRESHOLD = 80

def check_system():
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent
    if cpu_usage > CPU_THRESHOLD:
        print(f"Warning: CPU usage is high at {cpu_usage}%")
    else:
        print(f"CPU usage is normal at {cpu_usage}%")
    if mem_usage > MEM_THRESHOLD:
        print(f"Warning: Memory usage is high at {mem_usage}%")
    else:
        print(f"Memory usage is normal at {mem_usage}%")

if __name__ == "__main__":
    while True:
        check_system()
        time.sleep(5)  # Check every 5 seconds

