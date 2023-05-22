import json
from turtle import pd
from urllib import response
from utils import api_call , read_json_file
import pdb


def compare_api_request():
    try :
        data = read_json_file('response.json') 
    except Exception as e :
        return {}
    
    header = {'Authorization' : 'Basic c2tfdGVzdF81MU45aEdiU0MzMGhwR2JTUzRtT2JoV0FENGZ0anFCNldtV1VVTTQyb3BON3NJYlowR2lJQ2dZV1BCZFprOHBwUk1uRlZUdkNmZFcwUWZINzFGTjRQSU5WTzAwNnRvR3BMUWQ6'}
    
    body = json.dumps({'amount' : 100 , 'currency' : 'usd' , 'payment_method_types[]' : 'card'})
    response = api_call(
        url="https://api.stripe.com/v1/payment_intents" , 
        method="POST" , 
        header=header,
        body=body
    )
    print(response.status_code)    
    print(response.text)
    
    print(type(response.text))



def check_request(response_list):
    value_type_list = {}
    data_dict_map = {}
    for key , value in response_list.items() :
        if key == "data" :
            for k , v in value[0].items() : 
                if v is None :
                    v = ""
                data_dict_map.update({k : type(v)})      
        value_type_list.update({key : type(value)})
    
    return value_type_list , data_dict_map


def f(response_list):
    if len(response_list) < 2 :
        return "Invalid Data to Parse"
    parent_value_type_list , parent_data_dict = check_request(response_list[0])
    for dict in response_list:
        child_value_type_list , child_data_dict = check_request(dict)
        if parent_data_dict != child_data_dict :
            return False
        if parent_value_type_list != child_value_type_list :
            return False
    return True
        

        

def check_api_backward_compability():
    try:
        data = read_json_file('response.json')
    except Exception as e :
        return {"Exception Occured in Reading Json File"}
    
    response_list = data[0]
    request_list = data[1]
    ok =  f(response_list=response_list)
    ok_1 = f(response_list=request_list)
    print(ok_1)
    
    return ok

if __name__ == "__main__":
    print(1)
    