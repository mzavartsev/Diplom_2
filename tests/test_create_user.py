import pytest
from methods.user_methods import *

class TestCreateUser:
    def test_create_new_user(self, create_random_user_data, create_user):
        object_user_method = create_user.post_create_user(create_random_user_data)
        assert object_user_method[0] == 200
        auth = {"authorization":object_user_method[1]["accessToken"]}
        create_user.delete_user(auth)

    def test_create_new_user_with_already_used_creds(self, create_random_user_data, create_user):
        user = create_user.post_create_user(create_random_user_data)
        another_object_user_method = create_user.post_create_user(create_random_user_data)
        assert another_object_user_method[1]['message'] == 'User already exists'
        auth = {"authorization":user[1]["accessToken"]}
        create_user.delete_user(auth)

    @pytest.mark.parametrize("change_field", [
        ("email"),
        ("password"),
        ("name")
    ])
    def test_create_new_user_without_required_filed(self, change_field, create_random_user_data, create_user):
        del create_random_user_data[change_field]
        user_data = create_user.post_create_user(create_random_user_data)
        assert user_data[0] == 403

