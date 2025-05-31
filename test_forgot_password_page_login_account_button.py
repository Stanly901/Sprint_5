# Вход через кнопку в форме восстановления пароля

import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from test_data import test_user
from urls import BASE_URL, FORGOT_PASSWORD_PAGE, ACCOUNT_PROFILE_PAGE

@pytest.mark.usefixtures("driver", "wait")
class TestPasswordRecovery:

    def test_password_recovery_and_login(self, driver, wait):
        # 1. Переход на страницу восстановления пароля
        driver.get(f"{BASE_URL}{FORGOT_PASSWORD_PAGE}")

        # 2. Клик по кнопке "Войти" на странице восстановления пароля
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_LINK)).click()

        # 3. Заполнение поля Email на странице входа
        email_field = wait.until(EC.visibility_of_element_located(TestLocators.EMAIL_FIELD))
        email_field.send_keys(test_user["email"])

        # 4. Заполнение поля пароля
        password_field = wait.until(EC.visibility_of_element_located(TestLocators.PASSWORD_FIELD))
        password_field.send_keys(test_user["password"])

        # 5. Клик по кнопке "Войти"
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)).click()

        # 6. Клик по кнопке "Личный кабинет"
        wait.until(EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)).click()

        # 7. Ожидание перехода на страницу профиля
        wait.until(EC.url_contains(ACCOUNT_PROFILE_PAGE))

        # 8. Поиск поля с именем пользователя
        wait.until(EC.presence_of_element_located(TestLocators.NAME_INPUT))

        # 9. Проверка URL
        assert ACCOUNT_PROFILE_PAGE in driver.current_url, "Не перешли на страницу профиля"
