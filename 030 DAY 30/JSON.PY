import requests


response = requests.get(url = "https://api.kanye.rest/")
response.raise_for_status()
print(response.json()["quote"])