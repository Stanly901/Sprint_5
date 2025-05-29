# Вход через кнопку в форме восстановления пароля

import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("driver", "wait", "test_user")
class TestPasswordRecovery:

    def test_password_recovery_and_login(self, driver, wait, test_user):
        # 1. Переход на страницу восстановления пароля
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        # 2. Клик по кнопке "Войти" на странице восстановления пароля
        wait.until(EC.element_to_be_clickable(TestLocators.LOGIN_LINK)).click()

        # 3. Заполнение поля Email на странице входа в личный кабинет
        email_field = wait.until(EC.visibility_of_element_located(TestLocators.EMAIL_FIELD))
        email_field.send_keys(test_user["email"])

        # 4. Заполнение поля пароль на странице входа в личный кабинет
        password_field = driver.find_element(By.XPATH, TestLocators.PASSWORD_FIELD[1])
        password_field.send_keys(test_user["password"])

        # 4. Клик по кнопке "Войти" на странице входа в личный кабинет
        driver.find_element(By.XPATH, TestLocators.LOGIN_BUTTON[1]).click()

        # 5. Клик по кнопке "Личный кабинет" на главной странице
        account_button = wait.until(EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON))
        account_button.click()

        # 6. Ожидание перехода
        wait.until(EC.url_contains("/account/profile"))

        # 7. Поиск элемента с именем пользователя на странице "Личный кабинет"
        name_input = wait.until(EC.presence_of_element_located(TestLocators.NAME_INPUT))

        # 8. Проверка: нахождение на странице профиля
        assert "/account/profile" in driver.current_url, "Не перешли на страницу профиля"