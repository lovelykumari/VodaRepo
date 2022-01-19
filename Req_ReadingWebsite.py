#Add Package
import requests

#Prepare URL
url="https://api.github.com/users/lovely"

#Web REST API Calls (GET- HTTP VERB) Request
#response=requests.get(url,params={k:v},args)
r=requests.get(url)

#Fetch Reponse Content
print(r.content)
print(r.status_code)
print(r.url)