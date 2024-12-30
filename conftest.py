import pytest
from requests import *
from randomizer import *
from methods.user_methods import *

@pytest.fixture()
def create_random_user_data():
    user_data = return_login_password()
    return user_data

# @pytest.fixture()
# def registration_new_user(create_random_user_data):
#     created_user = UserMethods().post_create_user(create_random_user_data)
#     return created_user, create_random_user_data
