
servers = {
    "server1": 45,
    "server2": 90,
    "server3": 65,
    "server4": 95,
    "server5": 30
}

for server, cpu_usage in servers.items():
    if cpu_usage > 80:
        print(f"Warning: {server} has high CPU usage: {cpu_usage}%")
    else:
        print(f"{server} CPU usage is normal: {cpu_usage}%")

servers = {
    "server1": 45,
    "server2": 90
}

print(servers.keys())
print(servers.values())
print(servers.items())