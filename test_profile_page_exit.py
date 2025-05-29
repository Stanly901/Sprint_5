# Выход по кнопке «Выйти» в личном кабинете

from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import TestLocators

@pytest.mark.usefixtures("driver", "wait", "base_url", "test_user")
class TestLogoutFlow:

    def test_logout_flow(self, driver, wait, base_url, test_user):
        # 1. Открываем главную страницу
        driver.get(base_url)

        # 2. Кликаем по кнопке "Личный Кабинет"
        personal_account_button = wait.until(
            EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)
        )
        personal_account_button.click()

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

        # 5. Клик по кнопке "Личный кабинет"
        account_button = wait.until(
            EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # 6. Ожидаем вход
        wait.until(EC.url_contains("/account/profile"))

        # 7. Проверка успешного входа
        assert "/account/profile" in driver.current_url, f"Ожидался переход на профиль, но был: {driver.current_url}"

        # 8. Кликаем кнопку "Выход"
        logout_button = wait.until(
            EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        # 9. Ожидаем выход
        wait.until(EC.url_contains("/login"))

        # 10. Проверка: нахождение на странице входа
        assert "/login" in driver.current_url, f"После выхода должен быть редирект на /login, но был: {driver.current_url}"
