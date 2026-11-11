
import platform
import shutil
import psutil
import socket
import json
from datetime import datetime, timezone

def get_system_health():
    memory = psutil.virtual_memory()
    disk = shutil.disk_usage("/")
    cpu = psutil.cpu_percent(interval=1)

    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "hostname": socket.gethostname(),
        "os": platform.platform(),
        "python_version": platform.python_version(),
        "cpu_usage_percent": cpu,
        "memory_total_gb": round(memory.total / (1024 ** 3), 2),
        "memory_used_percent": memory.percent,
        "disk_total_gb": round(disk.total / (1024 ** 3), 2),
        "disk_used_percent": round(
            (disk.used / disk.total) * 100, 2
        ),
        "uptime_seconds": int(
            datetime.now().timestamp() - psutil.boot_time()
        )
    }

if __name__ == "__main__":
    health = get_system_health()
    print(json.dumps(health, indent=4))
