from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_user_login(driver, wait, base_url, test_user):

    # 1. Открываем главную страницу
    driver.get(base_url)

    # 2. Кликаем кнопку "Войти в аккаунт"
    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
        )
    )
    login_button.click()

    # 3. Заполняем поле Email
    email_field = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//label[text()='Email']/following-sibling::input")
        )
    )
    email_field.send_keys(test_user["email"])

    # 4. Заполняем поле Пароль
    password_field = driver.find_element(
        By.XPATH, "//input[@type='password']"
    )
    password_field.send_keys(test_user["password"])

    # 5. Кликаем кнопку "Войти"
    submit_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Войти')]")
        )
    )
    submit_button.click()

    # 6. Проверяем успешный вход
    wait.until(
        EC.url_contains("/account/profile")
    )