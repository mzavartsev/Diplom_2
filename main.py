import requests
from requests import *
from data import *


# URL = "https://stellarburgers.nomoreparties.site/api/auth/register"
#
# user_data = {"email": "211@yanex.ru",
# "password": "pass124122314124word",
# "name": "na124122134124me"}


# response0 = requests.post(f"{REGISTER_URL}", data=user_data)
# print(response0.status_code)
# print(response0.text)
# response1 = requests.post(f"{LOGIN_URL}", data=user_data)
# print(response1.status_code)
# print(response1.text)
# token = response1.json()["accessToken"]
# token2 = response1.json()["refreshToken"]
# print(token)
# auth = {"authorization":token}
# auth2 = {"token":token2}
# print(auth2)
# new_user_data = {"email": "2114124124234234234@yanex.ru"}
#
# response4 = requests.post("https://stellarburgers.nomoreparties.site/api/auth/logout", data=auth2)
# print(response4.status_code)
# print(response4.text)
#
# response3 = requests.patch(f"{USER_INFO_URL}", data=new_user_data, headers=auth)
# print(response3.status_code)
# print(response3.text)
#
# response2 = requests.get(f"{USER_INFO_URL}", headers=auth)
# print(response2.status_code)
# print(response2.text)

# respnce_product = requests.get(f"https://stellarburgers.nomoreparties.site/api/ingredients")
# print(respnce_product.status_code)
# print(respnce_product.text)
#
ingredient = {
"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa70"]
}

new_order = requests.get(f"https://stellarburgers.nomoreparties.site/api/orders")
print(new_order.status_code)
print(new_order.text)
