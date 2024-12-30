import pytest
import requests

from methods.user_methods import *


class TestModifyUser:
    @pytest.mark.parametrize("change_field, new_field", [
        ("email", "1tqw24awd1214214wd@ya.ru"),
        ("password", "qwerty"),
        ("name", "Maksim")
    ])
    def test_modify_info_authorization_user(self, change_field, new_field, create_random_user_data):
        user = UserMethods()
        user_data = user.post_create_user(create_random_user_data)
        access_token = {"authorization":user_data[1]["accessToken"]}
        new_user_data = {change_field:new_field}
        new_patched_user_info = user.patch_user_info(new_user_data, access_token)
        assert new_patched_user_info[0] == 200

    @pytest.mark.parametrize("change_field, new_field", [
        ("email", "1tqw2412fsew12412d@ya.ru"),
        ("password", "qwerty"),
        ("name", "Maksim")
    ])
    def test_modify_info_not_authorization_user(self,change_field, new_field, create_random_user_data):
        user = UserMethods()
        user_data = user.post_create_user(create_random_user_data)
        access_token = {"authorization":user_data[1]["accessToken"]}
        refresh_token = {"authorization":user_data[1]["refreshToken"]}
        new_user_data = {change_field:new_field}
        new_patched_user_info = user.patch_user_info(new_user_data, access_token)
        assert new_patched_user_info[0] == 200
