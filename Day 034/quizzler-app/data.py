from urllib import response
import requests

parameter = {
    "amount":10,
    "type":"boolean",
    "category":18
}

response = requests.get(url="https://opentdb.com/api.php",verify=False,params=parameter)
response.raise_for_status()
data = response.json()
question_data = data["results"]
