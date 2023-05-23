import json
from utils import ApiCall , JsonParser
from logger import log

if __name__ == "__main__" :
    log.info("main function invoked")
    
    url = "https://api.stripe.com/v1/customers/cus_NwXSjbTnBILlky"
    header = {"Authorization" : "Basic c2tfdGVzdF81MU45aEdiU0MzMGhwR2JTUzRtT2JoV0FENGZ0anFCNldtV1VVTTQyb3BON3NJYlowR2lJQ2dZV1BCZFprOHBwUk1uRlZUdkNmZFcwUWZINzFGTjRQSU5WTzAwNnRvR3BMUWQ6"}
    file_name = 'api_response.json'
    
    log.debug("url - %s" , url)
    log.debug("header - %s" , header)
  
    api_call = ApiCall(url=url , method="GET" ,  header = header)
    response = api_call.get()
    
    
    log.debug("response of STRIP-GET API Call - %s" , response)
    log.debug("status_code of STRIP-GET API Call - %s" , response.status_code)
    log.debug("body of STRIP-GET API Call - %s" , response.text)
    
    
    file_obj = JsonParser(file_name=file_name)
    json_data = file_obj.convert_fileto_json()
    
    log.debug("json-data %s" , json_data)
    print(type(json_data))
    dticc= json.loads(response.text)
    print(json_data==dticc)
    