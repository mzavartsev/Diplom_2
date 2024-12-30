import pytest
import requests

from methods.user_methods import *


class TestModifyUser:
    @pytest.mark.parametrize("change_field, new_field", [
        ("email", "1tqw24abddgfrd@ya.ru"),
        ("password", "qwerty"),
        ("name", "Maksim")
    ])
    def test_modify_info_authorization_user(self, change_field, new_field, create_random_user_data, get_auth_token):
        new_user_data = {change_field:new_field}
        new_patched_user_info = get_auth_token[0].patch_user_info(new_user_data, get_auth_token[1])
        assert new_patched_user_info[0] == 200

    @pytest.mark.parametrize("change_field, new_field", [
        ("email", "1tqw241awddb12d@ya.ru"),
        ("password", "qwerty"),
        ("name", "Maksim")
    ])
    def test_modify_info_not_authorization_user(self,change_field, new_field, create_random_user_data, get_auth_token):
        new_user_data = {change_field:new_field}
        new_patched_user_info = get_auth_token[0].patch_user_info(new_user_data, get_auth_token[1])
        assert new_patched_user_info[0] == 200
