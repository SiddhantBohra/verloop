import requests
import hashlib

email = "abhisidds@gmail.com"
result = hashlib.md5(email.encode())
print(result)
url = "https://hiring.verloop.io/api/github-challenge/start/"

payload = "{\n    \"email\": \"abhisidds@gmail.com\",\n    \"name\": \"Siddhant Bohra\",\n    \"angel_list\": \"https://angel.co/siddhant-bohra\",\n    \"github\": \"https://github.com/SiddhantBohra\"\n}"
headers = {
    'x-verloop-password': result.hexdigest(),
    'Content-Type': "application/json"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
