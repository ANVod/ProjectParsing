import requests

url = "https://api.github.com/search/repositories"
params = {"q": "Language:html"}
response = requests.get(url, params=params)
print(f"status code: {response.status_code}")
import json
print(json.dumps(response.json(), indent=4))
