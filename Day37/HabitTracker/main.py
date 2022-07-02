import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "<USER_GOES_HERE>"
TOKEN = "<TOKEN_GOES_HERE>"

GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# CREATE USER
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai",
}

# Injecting a token into an HTTP Header
headers = {
    "X-USER-TOKEN": TOKEN,
}

# CREATE GRAPH
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today_dt = dt.date.today()
#old_date = dt.datetime(year=2022, month=7, day=1)
# frmtd_date = old_date.strftime("%Y%m%d")
frmtd_date = today_dt.strftime("%Y%m%d")
# print(today)

pixel_post_config = {
    "date": frmtd_date,
    "quantity": "112",
}

# ADD DATA TO GRAPH
response = requests.post(url=post_pixel_endpoint, json=pixel_post_config, headers=headers)
print(response.text)
