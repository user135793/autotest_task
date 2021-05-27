import requests
import json
from requests.structures import CaseInsensitiveDict

url = 'http://bzteltestapi.pythonanywhere.com/'
def getToken():
    f = open('token.txt', 'r')
    t = f.read()
    f.close()
    return t

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
