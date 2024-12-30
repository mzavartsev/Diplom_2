import pytest
from randomizer import *
from methods.user_methods import *
from methods.order_methods import *


@pytest.fixture()
def create_random_user_data():
    user_data = return_login_password()
    return user_data

@pytest.fixture()
def create_order_object():
    order_object = OrderMethods()
    return order_object

@pytest.fixture()
def create_dict_with_ingredients_for_order(create_order_object):
    ingredients_dict = create_order_object.transform_ingredient_dict()
    ingredients_for_order = []
    ingredients_for_order.extend([ingredients_dict['Флюоресцентная булка R2-D3'],
                                  ingredients_dict['Биокотлета из марсианской Магнолии'],
                                  ingredients_dict['Соус Spicy-X']
                                  ])
    ingredients_for_order_dict = {"ingredients": ingredients_for_order}
    return create_order_object, ingredients_for_order_dict

@pytest.fixture()
def create_user():
    user = UserMethods()
    return user

@pytest.fixture()
def get_auth_token(create_user, create_random_user_data):
    auth_token = create_user.post_create_user(create_random_user_data)
    token = auth_token[1]["accessToken"]
    auth = {"authorization": token}
    yield create_user, auth
    create_user.delete_user(auth)