# Ошибка для некорректного пароля
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import TestLocators
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver", "wait", "base_url", "register_page_url", "invalid_user_data")
class TestRegistrationWithInvalidPassword:

    def test_registration_with_invalid_password(self, driver, wait, base_url, register_page_url, invalid_user_data):
        # 1. Открываем страницу регистрации
        driver.get(f"{base_url}{register_page_url}")

        # 2. Заполняем поле "Имя"
        name_field = wait.until(
            EC.visibility_of_element_located(TestLocators.REGISTRATION_NAME_FIELD)
        )
        name_field.send_keys(invalid_user_data["name"])

        # 3. Заполняем поле "Email"
        email_field = driver.find_element(*TestLocators.REGISTRATION_EMAIL_FIELD)
        email_field.send_keys(invalid_user_data["email"])

        # 4. Заполняем поле "Пароль"
        password_field = driver.find_element(*TestLocators.REGISTRATION_PASSWORD_FIELD)
        password_field.send_keys(invalid_user_data["password"])

        # 5. Кликаем кнопку "Зарегистрироваться"
        register_button = wait.until(
            EC.element_to_be_clickable(TestLocators.REGISTRATION_REGISTER_BUTTON)
        )
        register_button.click()

        # 6. Ожидаем сообщение об ошибке
        error_message = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//p[contains(@class, 'input__error') and contains(text(), '{invalid_user_data['expected_error']}')]")
            )
        )

        # 7. Проверка появления сообщения об ошибке
        assert invalid_user_data["expected_error"] in error_message.text, \
            f"Ожидалось сообщение '{invalid_user_data['expected_error']}', но сообщения об ошибке не было"