import pytest
import allure
from methods.user_methods import *


@allure.feature("ModifyUser")
class TestModifyUser:
    @allure.title("Изменение информации о пользователе")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/api/")
    @pytest.mark.parametrize("change_field, new_field", [
        ("email", "1tqw24xvdrd@ya.ru"),
        ("password", "qwerty"),
        ("name", "Maksim")
    ])
    def test_modify_info_authorization_user(self, change_field, new_field, create_random_user_data, get_auth_token):
        new_user_data = {change_field:new_field}
        new_patched_user_info = get_auth_token[0].patch_user_info(new_user_data, get_auth_token[1])
        assert new_patched_user_info[0] == 200

    @allure.title("Изменение информации о неавтризованном пользователе")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/api/")
    @pytest.mark.parametrize("change_field, new_field", [
        ("email", "1tqxvdd@ya.ru"),
        ("password", "qwerty"),
        ("name", "Maksim")
    ])
    def test_modify_info_not_authorization_user(self,change_field, new_field, create_random_user_data, get_auth_token):
        new_user_data = {change_field:new_field}
        new_patched_user_info = get_auth_token[0].patch_user_info(new_user_data, get_auth_token[1])
        assert new_patched_user_info[0] == 200
