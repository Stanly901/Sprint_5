# Успешная регистрация

import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from test_data import valid_user_data, get_random_email
from urls import BASE_URL, REGISTER_PAGE, LOGIN_PAGE, ACCOUNT_PROFILE_PAGE

@pytest.fixture
def random_email():
    return get_random_email()

def test_successful_registration(driver, wait, random_email):
    # 1. Открываем страницу регистрации
    driver.get(f"{BASE_URL}{REGISTER_PAGE}")

    # 2. Вводим имя
    name_field = wait.until(
        EC.visibility_of_element_located(TestLocators.REGISTRATION_NAME_FIELD)
    )
    name_field.send_keys(valid_user_data["name"])

    # 3. Вводим email
    email_field = driver.find_element(*TestLocators.REGISTRATION_EMAIL_FIELD)
    email_field.send_keys(random_email)

    # 4. Вводим пароль
    password_field = driver.find_element(*TestLocators.REGISTRATION_PASSWORD_FIELD)
    password_field.send_keys(valid_user_data["password"])

    # 5. Нажимаем кнопку "Зарегистрироваться"
    register_button = wait.until(
        EC.element_to_be_clickable(TestLocators.REGISTRATION_REGISTER_BUTTON)
    )
    register_button.click()

    # 6. Ожидаем переход на страницу входа
    wait.until(EC.url_contains(LOGIN_PAGE))

    # 7. Авторизация — вводим email и пароль
    email_field = wait.until(
        EC.visibility_of_element_located(TestLocators.LOGIN_EMAIL_FIELD)
    )
    email_field.send_keys(random_email)

    password_field = driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD)
    password_field.send_keys(valid_user_data["password"])

    # 8. Нажимаем кнопку "Войти"
    submit_button = wait.until(
        EC.element_to_be_clickable(TestLocators.LOGIN_SUBMIT_BUTTON)
    )
    submit_button.click()

    # 9. Кликаем "Личный кабинет"
    account_button = wait.until(
        EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)
    )
    account_button.click()

    # 10. Ожидаем переход в профиль
    wait.until(EC.url_contains(ACCOUNT_PROFILE_PAGE))

    # 11. Проверяем, что перешли в профиль
    assert ACCOUNT_PROFILE_PAGE in driver.current_url, (
        f"Ожидался переход на профиль, но текущий URL: {driver.current_url}"
    )