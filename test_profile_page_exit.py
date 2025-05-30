# Выход по кнопке «Выйти» в личном кабинете

from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from urls import BASE_URL
from test_data import test_user

def test_logout_flow(driver, wait):
    # 1. Открываем главную страницу
    driver.get(BASE_URL)

    # 2. Кликаем по кнопке "Личный Кабинет"
    personal_account_button = wait.until(
        EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)
    )
    personal_account_button.click()

    # 3. Вводим данные для входа
    email_field = wait.until(
        EC.visibility_of_element_located(TestLocators.EMAIL_FIELD)
    )
    email_field.send_keys(test_user["email"])

    password_field = driver.find_element(*TestLocators.PASSWORD_FIELD)
    password_field.send_keys(test_user["password"])

    # 4. Кликаем по кнопке "Войти"
    login_button = wait.until(
        EC.element_to_be_clickable(TestLocators.LOGIN_BUTTON)
    )
    login_button.click()

    # 5. Кликаем по кнопке "Личный кабинет" после входа
    account_button = wait.until(
        EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)
    )
    account_button.click()

    # 6. Ожидаем загрузки страницы профиля
    wait.until(EC.url_contains("/account/profile"))

    # 7. Проверка: пользователь находится на странице профиля
    assert "/account/profile" in driver.current_url, f"Ожидался переход на профиль, но был: {driver.current_url}"

    # 8. Кликаем по кнопке "Выход"
    logout_button = wait.until(
        EC.element_to_be_clickable(TestLocators.LOGOUT_BUTTON)
    )
    logout_button.click()

    # 9. Ожидаем редирект на страницу логина
    wait.until(EC.url_contains("/login"))

    # 10. Проверка: пользователь находится на странице логина
    assert "/login" in driver.current_url, f"После выхода должен быть редирект на /login, но был: {driver.current_url}"


