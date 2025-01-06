import pytest
import allure
from data import *


@allure.feature("GetOrder")
class TestGetOrder:
    @allure.title("Получение информации о заказе")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/api/")
    def test_get_info_about_order(self, create_random_user_data, get_auth_token, create_dict_with_ingredients_for_order):
        create_dict_with_ingredients_for_order[0].post_create_order(create_dict_with_ingredients_for_order[1])
        order_info = create_dict_with_ingredients_for_order[0].get_order_info(get_auth_token[1])
        assert order_info[0] == 200

    @allure.title("Получение информации о заказе без токена авторизации")
    @allure.link(BASE_URL, name="https://stellarburgers.nomoreparties.site/api/")
    def test_get_info_about_order_without_auth_token(self, create_dict_with_ingredients_for_order):
        create_dict_with_ingredients_for_order[0].post_create_order(create_dict_with_ingredients_for_order[1])
        order_info = create_dict_with_ingredients_for_order[0].get_order_info()
        assert order_info[0] == 401