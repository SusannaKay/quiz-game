import requests

ENDPOINT = "https://opentdb.com/api.php?"

parameters ={
    "amount":10,
    "type":"boolean"
}

response = requests.get(ENDPOINT,params=parameters)
response.raise_for_status()

data = response.json()
question_data = data['results']




