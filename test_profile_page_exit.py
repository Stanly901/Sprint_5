from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_logout_flow(driver, wait, base_url, test_user):

    # 1. Открываем главную страницу
    driver.get(base_url)

    # 2. Кликаем по кнопке "Личный Кабинет"
    personal_account_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Личный Кабинет']")
        )
    )
    personal_account_button.click()

    # 3. Заполняем форму авторизации
    email_field = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//label[text()='Email']/following-sibling::input")
        )
    )
    email_field.send_keys(test_user["email"])

    password_field = driver.find_element(By.XPATH, "//input[@type='password']")
    password_field.send_keys(test_user["password"])

    # 4. Кликаем кнопку "Войти"
    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Войти')]")
        )
    )
    login_button.click()

    # 5. Проверяем успешный вход
    wait.until(EC.url_contains("/account/profile"))

    # 6. Снова кликаем "Личный Кабинет"
    personal_account_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Личный Кабинет']")
        )
    )
    personal_account_button.click()

    # 7. Кликаем кнопку "Выход"
    logout_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']")
        )
    )
    logout_button.click()