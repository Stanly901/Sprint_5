# Ошибка для некорректного пароля

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import TestLocators
from test_data import invalid_user_data
from urls import BASE_URL, REGISTER_PAGE

def test_registration_with_invalid_password(driver, wait):
    # 1. Открываем страницу регистрации
    driver.get(f"{BASE_URL}{REGISTER_PAGE}")

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
        EC.visibility_of_element_located((
            By.XPATH,
            f"//p[contains(@class, 'input__error') and contains(text(), '{invalid_user_data['expected_error']}')]"
        ))
    )

    # 7. Проверка появления сообщения об ошибке
    assert invalid_user_data["expected_error"] in error_message.text, \
        f"Ожидалось сообщение об ошибке: '{invalid_user_data['expected_error']}', но было: '{error_message.text}'"