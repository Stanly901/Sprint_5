from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_successful_registration(driver, wait, base_url, register_page_url, valid_user_data):
    # 1. Открываем страницу регистрации
    driver.get(f"{base_url}{register_page_url}")

    # 2. Заполняем поле "Имя"
    name_field = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//label[text()='Имя']/following-sibling::input")
        )
    )
    name_field.send_keys(valid_user_data["name"])

    # 3. Заполняем поле "Email"
    email_field = driver.find_element(
        By.XPATH, "//label[text()='Email']/following-sibling::input"
    )
    email_field.send_keys(valid_user_data["email"])

    # 4. Заполняем поле "Пароль"
    password_field = driver.find_element(
        By.XPATH, "//input[@type='password']"
    )
    password_field.send_keys(valid_user_data["password"])

    # 5. Кликаем "Зарегистрироваться"
    register_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
        )
    )
    register_button.click()

    # 6. Проверяем успешную регистрацию (переход на страницу входа)
    wait.until(
        EC.url_contains("/login")
    )