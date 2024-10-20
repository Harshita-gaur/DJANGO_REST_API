import requests


endpoint="http://localhost:8000/api/products/36427364273/"
get_response=requests.get(endpoint)
print(get_response.json())
