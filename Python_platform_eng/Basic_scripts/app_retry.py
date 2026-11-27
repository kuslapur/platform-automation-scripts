import time

app_status = "DOWN"
max_retries = 5
retry = 1

while retry <= max_retries:
    print(f"Retry attempt: {retry}")

    if app_status == "UP":
        print("Application is UP and running")
        break

    print("Application is DOWN, retrying...")

    retry += 1
    time.sleep(2)

else:
    print("Max retry attempts reached. Application is still DOWN.")