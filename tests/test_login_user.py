import pytest
import allure
from methods.user_methods import *


@allure.feature("LoginUser")
class TestLoginUser:
    @allure.title("Авторизация пользователя")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/api/")
    def test_login_user(self, create_random_user_data, create_user):
        create_user.post_create_user(create_random_user_data)
        user_data = create_user.post_login_user(create_random_user_data)
        assert user_data[0] == 200
        auth = {"authorization":user_data[1]["accessToken"]}
        create_user.delete_user(auth)

    @allure.title("Авторизация пользователя с указанием неправильных кредов")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/api/")
    @pytest.mark.parametrize("change_field, new_field", [
        ("email", "1233211421412@yandex.ru"),
        ("password", "12345")
    ])
    def test_login_user_with_not_correct_pass(self, change_field, new_field, create_random_user_data, create_user):
        user = create_user.post_create_user(create_random_user_data)
        create_random_user_data[change_field] = new_field
        user_data = create_user.post_login_user(create_random_user_data)
        assert user_data[0] == 401
        auth = {"authorization":user[1]["accessToken"]}
        create_user.delete_user(auth)

