import pytest
from methods.user_methods import *


class TestLoginUser:
    def test_login_user(self, create_random_user_data, create_user):
        create_user.post_create_user(create_random_user_data)
        user_data = create_user.post_login_user(create_random_user_data)
        assert user_data[0] == 200
        auth = {"authorization":user_data[1]["accessToken"]}
        create_user.delete_user(auth)

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

