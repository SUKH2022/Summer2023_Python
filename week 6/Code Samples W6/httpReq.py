import requests

req = requests.get("https://www.georgiancollege.ca")
print(req.text)
print(f"Status: {req.status_code}")