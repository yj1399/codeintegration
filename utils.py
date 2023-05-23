from email import header
import json
import requests

# def api_call(url, **kwargs) :
#     response = {}
#     print(url)
#     print(kwargs)
#     if kwargs.get("method") == "GET" :
#         print("hi")
#         response = requests.get(url=url , params=kwargs.get("params") , headers=kwargs.get("header"))
#     elif kwargs.get("method") == "POST" :
#         print("hi")
#         print(kwargs.get("body"))
#         response = requests.post(url=url , data=kwargs.get("body") , headers=kwargs.get("header"))
#     else :
#         return {"response" : "Invalid Method Provided"}
#     return response
    

# def read_json_file(file_name):
#     f = open(file_name , "r")
#     data = json.loads(f.read())
#     return data

class ApiCall:
    def __init__(self , **kwargs):
        self.url = kwargs.get("url")
        self.method =  kwargs.get("method")
        self.params = kwargs.get("params")
        self.body = kwargs.get("body")
        self.header = kwargs.get("header")
        self.response = ""
        
        
    def get(self):
        try :
            self.response = requests.get(url=self.url , params=self.params , headers=self.header)
        except Exception as e :
            return {"Exception Occured in Get Api Call"}
        
        return self.response
    
    def post(self):
        try :
            self.response = requests.post(url=self.url , data=self.body , headers=self.header)
        except Exception as e :
            return {"Exception Occured in Post Api Call"}
        
        return self.response

class JsonParser:
    def __init__(self , **kwargs):
        self.file_name = kwargs.get("file_name")
        
    def convert_fileto_json(self):
        f = open(self.file_name , "r")
        data = json.loads(f.read())
        return data

