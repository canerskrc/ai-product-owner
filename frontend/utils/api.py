import requests

BASE_URL = "http://localhost:8000"

def post(path: str, data: dict):
    try:
        response = requests.post(BASE_URL + path, json=data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"API error: {e}")
        return None