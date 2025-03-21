import requests
import json

url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)

reponse_dict = r.json()
response_string = json.dumps(reponse_dict, indent=4)
print(response_string)