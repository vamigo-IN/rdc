import requests

url = "https://script.google.com/macros/s/AKfycbxmyth4RrdD-DcZRnOx-w63yb2wdxPeb1ZbgYUHUXvjY-OuCwWWaajg4tLu0ZgBKIlL/exec"
data = {
    "name": "Test User",
    "phone": "1234567890",
    "treatment": "Test",
    "time": "Any",
    "source": "Test Script"
}

response = requests.post(url, json=data, allow_redirects=True)
print("Status Code:", response.status_code)
print("Response:", response.text)
