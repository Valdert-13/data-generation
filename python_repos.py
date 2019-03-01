import requests

url =''

r = requests.get(url)

print ('Status code', r.status_code)

response_dict = r.json()

print(response_dict.keys())


