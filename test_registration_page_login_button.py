from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_login_from_register_page(driver, wait, base_url, user_credentials, register_page_url, profile_page_url):

    # 1. Открываем страницу регистрации
    driver.get(f"{base_url}{register_page_url}")

    # 2. Кликаем по ссылке "Войти"
    login_link = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and text()='Войти']")
        )
    )
    login_link.click()

    # 3. Заполняем форму авторизации
    email_field = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//label[text()='Email']/following-sibling::input")
        )
    )
    email_field.send_keys(user_credentials["email"])

    password_field = driver.find_element(By.XPATH, "//input[@type='password']")
    password_field.send_keys(user_credentials["password"])

    # 4. Кликаем по кнопке "Войти"
    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Войти')]")
        )
    )
    login_button.click()

    # 5. Проверяем успешный вход
    wait.until(
        EC.url_contains(profile_page_url)
    )