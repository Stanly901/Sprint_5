# Вход по кнопке «Войти в аккаунт» на главной

import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from urls import BASE_URL, ACCOUNT_PROFILE_PAGE
from test_data import test_user

@pytest.mark.usefixtures("driver", "wait")
class TestUserLogin:

    def test_user_can_login_and_access_profile(self, driver, wait):
        # 1. Открытие главной страницы
        driver.get(BASE_URL)

        # 2. Клик по кнопке "Войти в аккаунт"
        login_button = wait.until(
            EC.element_to_be_clickable(TestLocators.LOGIN_PAGE_LOGIN_BUTTON)
        )
        login_button.click()

        # 3. Заполнение поля Email
        email_field = wait.until(
            EC.visibility_of_element_located(TestLocators.EMAIL_FIELD)
        )
        email_field.send_keys(test_user["email"])

        # 4. Заполнение поля Пароль
        password_field = driver.find_element(*TestLocators.PASSWORD_FIELD)
        password_field.send_keys(test_user["password"])

        # 5. Клик по кнопке "Войти"
        submit_button = wait.until(
            EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)
        )
        submit_button.click()

        # 6. Клик по кнопке "Личный кабинет"
        account_button = wait.until(
            EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # 7. Ожидание перехода на страницу профиля
        wait.until(EC.url_contains(ACCOUNT_PROFILE_PAGE))

        # 8. Проверка: переход успешен
        assert ACCOUNT_PROFILE_PAGE in driver.current_url, (
            f"Ожидался переход на страницу профиля, но текущий URL: {driver.current_url}"
        )