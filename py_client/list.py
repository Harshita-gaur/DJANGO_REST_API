import requests
from getpass import getpass


auth_endpoint="http://localhost:8000/api/auth/"
username=input("Username:\n")
password=getpass("Password:\n")
auth_response=requests.post(auth_endpoint,json={'username':'harshita','password':password})
print(auth_response.json())

if auth_response.status_code==200:
    token=auth_response.json()['token']
    headers={
        "Authorisation":f"Token{token}"
        # "Authorisation":f"Bearer {token}"  
    }
    endpoint="http://localhost:8000/api/products/"
    get_response=requests.get(endpoint,headers=headers)
    # print(get_response.json())
    
    data = get_response.json()
    next_url = data['next']
    results = data['results']
    print("next_url", next_url)
    print(results)
    # if next_url is not None:
    #     get_response = requests.get(next_url, headers=headers) 
    # print()