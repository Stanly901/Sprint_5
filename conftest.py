import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="class") # Настройка драйвера перед тестом
def driver():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="class") # ожидание в 10 секунд после выполнения действия
def wait(driver):
    return WebDriverWait(driver, 10)

@pytest.fixture(scope="class") # данные учетки
def test_user():
    return {
        "email": "bondarenko232323@ya.ru",
        "password": "123456"
    }

@pytest.fixture(scope="class") # возвращение на главную страницу
def base_url():
    return "https://stellarburgers.nomoreparties.site"

@pytest.fixture(scope="class") # данные учетки не валидные
def invalid_user_data():
    return {
        "name": "Иван",
        "email": "bondarenko232323@ya.ru",
        "password": "12345",
        "expected_error": "Некорректный пароль"
    }

@pytest.fixture(scope="class") # разделы перехода
def sections():
    return ["Булки", "Соусы", "Начинки"]

@pytest.fixture(scope="class") # URL страницы регистрации
def register_page_url():
    return "/register"

@pytest.fixture(scope="class") # данными для регистрации
def valid_user_data():
    return {
        "name": "Иван",
        "password": "1234567"
    }

@pytest.fixture(scope="function") # генерация случайного email
def random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{username}@example.com"