import pytest
import requests
from methods.order_methods import *


class TestCreateOrder:
    def test_create_new_order_with_ingredients(self, create_dict_with_ingredients_for_order):
        new_order = create_dict_with_ingredients_for_order[0].post_create_order(create_dict_with_ingredients_for_order[1])
        assert new_order[0] == 200

    def test_create_new_order_without_ingredients(self, create_order_object):
        ingredients_for_order_dict = {"ingredients":[]}
        new_order = create_order_object.post_create_order(ingredients_for_order_dict)
        assert new_order[0] == 400

    def test_create_new_order_with_incorrect_ingredients_hash(self, create_order_object):
        ingredients_for_order_dict = {"ingredients": ["61c0c5a71d1f82001bdaa111"]}
        new_order = create_order_object.post_create_order(ingredients_for_order_dict)
        assert new_order[0] == 400
