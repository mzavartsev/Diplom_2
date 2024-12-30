import pytest
from methods.user_methods import *

class TestCreateUser:
    def test_create_new_user(self, create_random_user_data):
        object_user_method = UserMethods().post_create_user(create_random_user_data)
        assert object_user_method[0] == 200

    def test_create_new_user_with_already_used_creds(self, create_random_user_data):
        UserMethods().post_create_user(create_random_user_data)
        another_object_user_method = UserMethods().post_create_user(create_random_user_data)
        assert another_object_user_method[1]['message'] == 'User already exists'

    @pytest.mark.parametrize("change_field", [
        ("email"),
        ("password"),
        ("name")
    ])
    def test_create_new_user_without_required_filed(self, change_field, create_random_user_data, create_user):
        del create_random_user_data[change_field]
        user_data = create_user.post_create_user(create_random_user_data)
        assert user_data[0] == 403

