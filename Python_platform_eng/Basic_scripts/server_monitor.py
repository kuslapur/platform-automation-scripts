servers = {
    "web-01": "UP",
    "web-02": "DOWN",
    "app-01": "UP",
    "app-02": "DOWN",
    "db-01": "UP"
}

for server, status in servers.items():

    if status == "UP":
        print(f"{server} is healthy")

    else:
        print(f"ALERT: {server} is DOWN")