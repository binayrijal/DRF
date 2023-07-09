import requests
import json
URL=""

def getdata(id=None):
    id={}
    if id is not None:
        data={'id':id}
        json_data=json.dumps(data)
        r=requests.get(url=URL,data=json_data)
        data=r.json()
        print(data)

getdata()