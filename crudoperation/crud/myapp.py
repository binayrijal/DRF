import requests
import json
URL="http://127.0.0.1:8000/crudstart/view_student/"

def getdata(id = None):
    data={}

    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)

#getdata(10)

def postdata():
    data={
        'name':'atit',
        'roll':20,
        'city':'koteshwor',
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    data=r.json()
    print(data)
#postdata()

def putdata():
    data={
        'id':11,
        'name':'amit', 
        'roll':191508, #for partial update we send only partial data in our case we send id,name and city roll is in this because i change code for fully update from previous partial update
        'city':'kharibot'
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)
putdata()

def deletedata():
    data={
        'id':13
    }
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)
#deletedata()