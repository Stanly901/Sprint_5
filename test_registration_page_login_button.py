# Вход через кнопку в форме регистрации

from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import TestLocators

@pytest.mark.usefixtures("driver", "wait", "base_url", "test_user", "register_page_url")
class TestLoginFromRegisterPage:

    def test_login_from_register_page(self, driver, wait, base_url, test_user, register_page_url):
        # 1. Открываем страницу регистрации
        driver.get(f"{base_url}{register_page_url}")

        # 2. Кликаем по ссылке "Войти"
        login_link = wait.until(
            EC.element_to_be_clickable(TestLocators.LOGIN_LINK)
        )
        login_link.click()

        # 3. Заполняем форму авторизации
        email_field = wait.until(
            EC.visibility_of_element_located(TestLocators.EMAIL_FIELD)
        )
        email_field.send_keys(test_user["email"])

        password_field = driver.find_element(*TestLocators.PASSWORD_FIELD)
        password_field.send_keys(test_user["password"])

        # 4. Кликаем кнопку "Войти"
        submit_button = wait.until(
            EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)
        )
        submit_button.click()

        # 5. Клик по кнопке "Личный кабинет"
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