import requests

url = "https://bkuslapur.online/"

def check_api_health():
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(f"API is healthy. Status code: {response.status_code}")

        else:
            print(f"API is unhealthy. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error checking API health: {e}")

if __name__ == "__main__":
    check_api_health()
        