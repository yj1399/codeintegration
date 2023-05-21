import json
from urllib import response
from utils import api_call , read_json_file



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


if __name__ == "__main__":
    compare_api_request()