"""HARD - Doing HTTP requests"""

# pip install requests

# Solution 1 - my
import json
import requests

try:
    response = requests.get("https://api.github.com/users/python", timeout=10)
except requests.RequestException:
    print("No internet connectivity.")
else:
    print(json.dumps(response.json(), indent=2))


# Solution 2
import requests

try:
    print(requests.get("https://api.github.com/users/python", timeout=10).text)
except requests.RequestException:
    print("No internet connectivity.")
