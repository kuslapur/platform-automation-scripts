def get_token():
    with open("D:/python/token.txt", "r") as f:
        return f.read().strip()