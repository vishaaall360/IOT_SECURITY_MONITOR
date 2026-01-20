import time
import random
import requests

SERVER_URL = "http://127.0.0.1:5000/data"

while True:
    data = {
        "motion": random.choice([0, 1]),
        "temperature": random.randint(20, 60),
        "gas": random.randint(100, 500)
    }

    try:
        requests.post(SERVER_URL, json=data)
        print("Sent:", data)
    except:
        print("Server not running")

    time.sleep(3)
