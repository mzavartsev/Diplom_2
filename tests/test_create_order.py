import pytest
import requests
from methods.order_methods import *


class TestCreateOrder:
    def test_create_new_order_with_ingredients(self):
        order_object = OrderMethods()
        ingredients_dict = order_object.transform_ingredient_dict()
        ingredients_for_order = []
        ingredients_for_order.extend([ingredients_dict['Флюоресцентная булка R2-D3'],
                                      ingredients_dict['Биокотлета из марсианской Магнолии'],
                                      ingredients_dict['Соус Spicy-X']
                                      ])
        ingredients_for_order_dict = {"ingredients":ingredients_for_order}
        new_order = order_object.post_create_order(ingredients_for_order_dict)
        assert new_order[0] == 200

    def test_create_new_order_without_ingredients(self):
        order_object = OrderMethods()
        ingredients_for_order_dict = {"ingredients":[]}
        new_order = order_object.post_create_order(ingredients_for_order_dict)
        assert new_order[0] == 400

    def test_create_new_order_with_incorrect_ingredients_hash(self):
        order_object = OrderMethods()
        ingredients_for_order_dict = {"ingredients": ["61c0c5a71d1f82001bdaa111"]}
        new_order = order_object.post_create_order(ingredients_for_order_dict)
        assert new_order[0] == 400
