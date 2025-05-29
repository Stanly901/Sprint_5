# Переход по клику на «Личный кабинет»

import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

@pytest.mark.usefixtures("driver", "wait", "base_url")
class TestPersonalAccountNavigation:

    def test_navigate_to_login_from_main_page(self, driver, wait, base_url):
        # 1. Переходим на главную страницу
        driver.get(base_url)

        # 2. Кликаем по кнопке "Личный Кабинет" на главной странице
        account_button = wait.until(
            EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # 3. Ожидание перехода на страницу авторизации
        wait.until(EC.url_contains("/login"))

        # 4. Проверка: нахождение на странице авторизации
        assert "/login" in driver.current_url, (
            f"Ожидался переход на страницу логина, но текущий URL: {driver.current_url}"
        )