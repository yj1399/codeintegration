from email import header
import json
import requests

def api_call(url, **kwargs) :
    response = {}
    print(url)
    print(kwargs)
    if kwargs.get("method") == "GET" :
        print("hi")
        response = requests.get(url=url , params=kwargs.get("params") , headers=kwargs.get("header"))
    elif kwargs.get("method") == "POST" :
        print("hi")
        print(kwargs.get("body"))
        print(kwargs.get("headers"))
        response = requests.post(url=url , data=kwargs.get("body") , headers=kwargs.get("header"))
    else :
        return {"response" : "Invalid Method Provided"}
    return response
    

def read_json_file(file_name):
    f = open(file_name , "r")
    data = json.loads(f.read())
    return data