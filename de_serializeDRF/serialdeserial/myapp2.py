import requests
import json
URL="http://127.0.0.1:8000/deserial/viewdeserial"
dictdata={
    'name':'binay',
    'roll':'111',
    'address':'bhaktapur'
    }
json_data=json.dumps(dictdata)
r=requests.post(url=URL,data=json_data)
data=r.json()
print(data)