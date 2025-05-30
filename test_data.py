
import random
import string

def get_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{username}@example.com"

test_user = {
    "email": "bondarenko232323@ya.ru",
    "password": "123456"
}

invalid_user_data = {
    "name": "Иван",
    "email": "bondarenko232323@ya.ru",
    "password": "12345",
    "expected_error": "Некорректный пароль"
}

valid_user_data = {
    "name": "Иван",
    "password": "1234567"
}

sections = ["Булки", "Соусы", "Начинки"]

register_page_url = "/register"

base_url = "https://stellarburgers.nomoreparties.site"