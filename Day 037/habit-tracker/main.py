import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = ""
USERNAME = "parz"
GRAPHID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes",
}

#response = requests.post(url=pixela_endpoint,json=user_params,verify=False)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPHID,
    "name" :"Cycling Graph",
    "unit": "Km",
    "type":"float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint,json=graph_config,headers=headers,verify=False)
#print(response.text)

today = datetime.now()


createpixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

pixel_config = {
    "date":today.strftime('%Y%m%d'),
    "quantity":input("How many KMS you ran today: "),
}

response = requests.post(url=createpixel_endpoint,verify=False,headers=headers,json=pixel_config)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime('%Y%m%d')}"

pixel_config = {
    "quantity":"20",
}

#response = requests.put(url=update_endpoint,verify=False,headers=headers,json=pixel_config)
#print(response.text)

# Delete pixel
#response = requests.delete(url=update_endpoint,verify=False,headers=headers)
#print(response.text)