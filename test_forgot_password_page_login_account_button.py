from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_password_recovery_and_login(driver, wait, test_user):

    # 1. Переход на страницу восстановления пароля
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    # 2. Клик по кнопке "Войти"
    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and text()='Войти']")
    )).click()

    # 3. Заполнение полей авторизации
    email_field = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//label[text()='Email']/following-sibling::input")
    ))
    email_field.send_keys(test_user["email"])

    password_field = driver.find_element(By.XPATH, "//input[@type='password']")
    password_field.send_keys(test_user["password"])

    # 4. Клик по кнопке входа
    driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()

    # 5. Проверка входа
    wait.until(EC.url_contains("/account/profile"))