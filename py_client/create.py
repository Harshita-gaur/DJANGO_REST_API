import requests

headers={
    'Authorization':'Token 1b8f3ad3da7242a5179def10d5fa598a58455aa8'
}


endpoint="http://localhost:8000/api/products/"
data={
    "title":"the required field",
    "price":42.99,
    "sale_price":50.00
}
get_response=requests.post(endpoint,json=data,headers=headers)
print(get_response.json())