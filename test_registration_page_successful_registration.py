# Успешная регистрация

import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators  # Импортируем локаторы

@pytest.mark.usefixtures("driver", "wait", "base_url", "register_page_url", "valid_user_data", "random_email")
class TestSuccessfulRegistration:

    def test_successful_registration(self, driver, wait, base_url, register_page_url, valid_user_data, random_email):
        # 1. Открываем страницу регистрации
        driver.get(f"{base_url}{register_page_url}")

        # 2. Заполняем поле "Имя"
        name_field = wait.until(
            EC.visibility_of_element_located(TestLocators.REGISTRATION_NAME_FIELD)
        )
        name_field.send_keys(valid_user_data["name"])

        # 3. Заполняем поле "Email"
        email_field = driver.find_element(*TestLocators.REGISTRATION_EMAIL_FIELD)
        email_field.send_keys(random_email)

        # 4. Заполняем поле "Пароль"
        password_field = driver.find_element(*TestLocators.REGISTRATION_PASSWORD_FIELD)
        password_field.send_keys(valid_user_data["password"])

        # 5. Кликаем на кнопку "Зарегистрироваться"
        register_button = wait.until(
            EC.element_to_be_clickable(TestLocators.REGISTRATION_REGISTER_BUTTON)
        )
        register_button.click()

        # 6. Ожидание перехода на страницу авторизации
        wait.until(EC.url_contains("/login"))

        # 7. Вводим логин Email и пароль
        email_field = wait.until(
            EC.visibility_of_element_located(TestLocators.LOGIN_EMAIL_FIELD)
        )
        email_field.send_keys(random_email)

        password_field = driver.find_element(*TestLocators.LOGIN_PASSWORD_FIELD)
        password_field.send_keys(valid_user_data["password"])

        # 8. Кликаем кнопку "Войти"
        submit_button = wait.until(
            EC.element_to_be_clickable(TestLocators.LOGIN_SUBMIT_BUTTON)
        )
        submit_button.click()

        # 9. Клик по кнопке "Личный кабинет"
        account_button = wait.until(
            EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # 10. Ожидаем переход на страницу профиля
        wait.until(EC.url_contains(TestLocators.PROFILE_PAGE_URL))

        # 11. Проверка: нахождение на странице профиля
        assert TestLocators.PROFILE_PAGE_URL in driver.current_url, (
            f"Ожидался переход на страницу профиля, но текущий URL: {driver.current_url}"
        )