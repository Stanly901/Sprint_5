# Вход через кнопку «Личный кабинет»

import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from urls import BASE_URL, ACCOUNT_PROFILE_PAGE
from test_data import test_user

@pytest.mark.usefixtures("driver", "wait")
class TestLoginFlow:

    def test_login_via_personal_account(self, driver, wait):
        # 1. Открываем главную страницу
        driver.get(BASE_URL)

        # 2. Кликаем по кнопке "Личный Кабинет"
        account_button = wait.until(
            EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # 3. Заполняем форму авторизации
        email_field = wait.until(
            EC.visibility_of_element_located(TestLocators.EMAIL_FIELD)
        )
        email_field.send_keys(test_user["email"])

        password_field = driver.find_element(*TestLocators.PASSWORD_FIELD)
        password_field.send_keys(test_user["password"])

        # 4. Кликаем кнопку "Войти"
        login_button = wait.until(
            EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)
        )
        login_button.click()

        # 5. Снова кликаем по "Личный кабинет"
        account_button = wait.until(
            EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # 6. Ожидаем переход на страницу профиля
        wait.until(EC.url_contains(ACCOUNT_PROFILE_PAGE))

        # 7. Проверка: находимся на странице профиля
        assert ACCOUNT_PROFILE_PAGE in driver.current_url, (
            f"Ожидался переход на страницу профиля, но текущий URL: {driver.current_url}"
        )


