import requests

# Base URL for the FastAPI server
#BASE_URL = "https://chatbotbackend-c3894ac9dd9a.herokuapp.com"
BASE_URL = "http://localhost:8010"


def get_response_model(context,question):
    url=f"{BASE_URL}/responsechatbot"
    
    data = {
    "context": context,
    "question":question
    }
    response=requests.post(url,json=data)
    if response.status_code==200:
        return response.json()
    else: 
        #Handle errors
        raise Exception(f"Failed to retrieve the response from the model.Something wrong happened!")
    
