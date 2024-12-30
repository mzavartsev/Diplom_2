import requests
from data import *


class OrderMethods:

    def post_create_order(self, ingredients):
        new_order = requests.post(f"{ORDER_URL}", data=ingredients)
        return new_order.status_code, new_order.json(), new_order.text

    def get_order_info(self, auth_token=None):
        if auth_token is not None:
            order_info = requests.get(f"{ORDER_URL}", headers=auth_token)
        else:
            order_info = requests.get(f"{ORDER_URL}")
        return order_info.status_code, order_info.json(), order_info.text

    def get_ingredirnt_dict(self):
        get_dict_with_all_ingredients = requests.get(f"{GET_INGREDIENT_URL}")
        return get_dict_with_all_ingredients.json()

    def transform_ingredient_dict(self):
        all_dict = self.get_ingredirnt_dict()
        transformed_dict = {}
        for item in all_dict["data"]:
            name = item["name"]
            id = item["_id"]
            transformed_dict[name] = id
        return transformed_dict

o = OrderMethods()
print(o.transform_ingredient_dict())