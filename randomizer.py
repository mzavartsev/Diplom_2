import random
import string


def return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    name = generate_random_string(10)
    password = generate_random_string(10)
    email = generate_random_string(10)

    payload = {
        "name": name,
        "password": password,
        "email": email + "@yandex.ru"
    }

    return payload