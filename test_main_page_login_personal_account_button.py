from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_login_via_personal_account(driver, wait, base_url, user_credentials):

    # 1. Открываем главную страницу
    driver.get(base_url)

    # 2. Кликаем по кнопке "Личный Кабинет"
    account_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Личный Кабинет']")
        )
    )
    account_button.click()

    # 3. Заполняем форму авторизации
    email_field = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//label[text()='Email']/following-sibling::input")
        )
    )
    email_field.send_keys(user_credentials["email"])

    password_field = driver.find_element(By.XPATH, "//input[@type='password']")
    password_field.send_keys(user_credentials["password"])

    # 4. Кликаем кнопку "Войти"
    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Войти')]")
        )
    )
    login_button.click()

    # 5. Проверяем результат в зависимости от типа тестовых данных
    if user_credentials["is_valid"]:
        wait.until(EC.url_contains("/account/profile"))
    else:
        error_message = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//p[contains(@class, 'input__error')]")
            )
        )