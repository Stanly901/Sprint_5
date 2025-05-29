# Вход через кнопку «Личный кабинет»

import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

@pytest.mark.usefixtures("driver", "wait", "base_url", "test_user")
class TestLoginViaPersonalAccount:

    def test_login_via_personal_account(self, driver, wait, base_url, test_user):
        # 1. Открываем главную страницу
        driver.get(base_url)

        # 2. Кликаем по кнопке "Личный Кабинет"
        account_button = wait.until(
            EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # 3. Заполняем форму авторизации на странице авторизации
        email_field = wait.until(
            EC.visibility_of_element_located(TestLocators.EMAIL_FIELD)
        )
        email_field.send_keys(test_user["email"])

        password_field = driver.find_element(*TestLocators.PASSWORD_FIELD)
        password_field.send_keys(test_user["password"])

        # 4. Кликаем кнопку "Войти" на странице авторизации
        login_button = wait.until(
            EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)
        )
        login_button.click()

        # 5. Клик по кнопке "Личный кабинет" на главной странице
        account_button = wait.until(
            EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # 6. Ожидаем переход на страницу профиля
        wait.until(EC.url_contains("/account/profile"))

        # 7. Проверка: нахождение на странице профиля
        assert "/account/profile" in driver.current_url, (
            f"Ожидался переход на страницу профиля, но текущий URL: {driver.current_url}"
        )