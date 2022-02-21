import requests
from pprint import pprint as print

API = "114a73f8b304aaedc972149d"
currency = 'USD'
URL = f"https://v6.exchangerate-api.com/v6/{API}/latest/{currency}"

response = requests.get(URL)
print(response.status_code)
print(response.json())