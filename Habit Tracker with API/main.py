import requests
from datetime import datetime

# Credentials Here
GRAPHID = ""
TOKEN = ""
USERNAME = ""
pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN,
}

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHID,
    "name": "Hours of Coding",
    "unit": "hours",
    "type": "int",
    "color": "kuro",
}
# response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

my_date = datetime.now()
today = my_date.strftime("%Y%m%d")

post_pixel_params = {
    "date": today,
    "quantity": input("How many hours did you Code today?: "),
}

# response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today}"

update_data = {
    "quantity": "4",
}
# response = requests.put(url=update_pixel_endpoint, json=update_data, headers=headers)
# print(response.text)
