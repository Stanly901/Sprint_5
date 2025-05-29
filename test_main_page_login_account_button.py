# Вход по кнопке «Войти в аккаунт» на главной

import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

@pytest.mark.usefixtures("driver", "wait", "base_url", "test_user")
class TestUserLogin:

    def test_user_can_login_and_access_profile(self, driver, wait, base_url, test_user):
        # 1. Открываем главную страницу
        driver.get(base_url)

        # 2. Кликаем кнопку "Войти в аккаунт"
        login_button = wait.until(
            EC.element_to_be_clickable(TestLocators.LOGIN_PAGE_LOGIN_BUTTON)
        )
        login_button.click()

        # 3. Заполняем поле Email на странице авторизации
        email_field = wait.until(
            EC.visibility_of_element_located(TestLocators.EMAIL_FIELD)
        )
        email_field.send_keys(test_user["email"])

        # 4. Заполняем поле Пароль на странице авторизации
        password_field = driver.find_element(*TestLocators.PASSWORD_FIELD)
        password_field.send_keys(test_user["password"])

        # 5. Кликаем кнопку "Войти" на странице авторизации
        submit_button = wait.until(
            EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)
        )
        submit_button.click()

        # 6. Клик по кнопке "Личный кабинет" на главной странице
        account_button = wait.until(
            EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # 7. Ожидаем переход на страницу профиля
        wait.until(EC.url_contains("/account/profile"))

        # 8. Проверка: нахождение на странице профиля
        assert "/account/profile" in driver.current_url, (
            f"Ожидался переход на страницу профиля, но текущий URL: {driver.current_url}"
        )