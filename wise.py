import requests

API_TOKEN = "e895b40d-834c-47db-9105-22ebc4a13914"

url = f"https://api.wise-sandbox.com/v1/profiles"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

response = requests.post(url, headers=headers)

print(response.json())
