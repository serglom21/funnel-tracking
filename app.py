import requests
from random import randint

base_url = "http://127.0.0.1:5000"
endpoints = ['/launch', '/verse', '/scripture', '/prayer', '/plan', '/donation']

def simulate_user():
    for i in range(randint(1, len(endpoints))):
        response = requests.get(base_url + endpoints[i])
        print(response.text)

if __name__ == "__main__":
    for _ in range(15):  # Simulating 15 users
        simulate_user()