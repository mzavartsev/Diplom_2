import pytest
import requests
from requests import *
from data import *


class UserMethods:

    def post_create_user(self, user_data):
        user = requests.post(f"{REGISTER_URL}", data=user_data)
        return user.status_code, user.json(), user.text

    def post_login_user(self, user_data):
        login_user = requests.post(f"{LOGIN_URL}", data=user_data)
        return login_user.status_code, login_user.json(), login_user.text

    def get_user_info(self, auth):
        user_info = requests.get(f"{USER_INFO_URL}", headers=auth)
        return user_info.status_code, user_info.json(), user_info.text

    def patch_user_info(self, user_data, auth):
        patched_user_info = requests.patch(f"{USER_INFO_URL}", data=user_data, headers=auth)
        return patched_user_info.status_code, patched_user_info.json(), patched_user_info.text