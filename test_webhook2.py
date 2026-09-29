import requests
import json

url = "https://script.google.com/macros/s/AKfycbxmyth4RrdD-DcZRnOx-w63yb2wdxPeb1ZbgYUHUXvjY-OuCwWWaajg4tLu0ZgBKIlL/exec"
data = {
    "name": "Test User",
    "phone": "1234567890",
    "treatment": "Test",
    "time": "Any",
    "source": "Test Script Plain Text"
}

headers = {'Content-Type': 'text/plain;charset=utf-8'}
response = requests.post(url, data=json.dumps(data), headers=headers, allow_redirects=True)
print("Status Code:", response.status_code)
print("Response:", response.text)
