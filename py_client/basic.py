#has no relation to django,framework ,python backend or even the endpoint. It just uses python to interact with the Api
import requests

# endpoint="https://github.com/"
# endpoint="https://httpbin.org/status/200"
# endpoint="https://httpbin.org/"    #HTTP request ,it gives an HTML response
# endpoint="https://httpbin.org/anything"    #REST API (still an HTTP) request ,it gives an JSON response
endpoint = "http://localhost:8000/api/"
endpoint = "http://localhost:8000/api/?this_arg=this_value"# parameter and value

#library API 
# REST APIs area kind of web based API
# get_response=requests.get(endpoint)
# print(get_response.text) #prints the raw text response code
# get_response=requests.get(endpoint,jsonprint(get_response.json())={"query":"Hello world"})
# get_response=requests.get(endpoint,params={"abc":123},jsonprint(get_response.json())={"query":"Hello world"})

# print(get_response.json()) # now prints python dictionary ,only differenece being json=none ,earlier it was null
# print(get_response.status_code) 
# print(get_response.json()['message'])
# get_response=requests.get(endpoint,data={"query":"Hello world"}) # difference: data,content-type,form
get_response=requests.post(endpoint,json={"title":"abc123","content":"Hello World"}) 

print(get_response.json()) # difference: 'data': '{"query": "Hello world"}'

