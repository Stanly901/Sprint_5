# Переход по клику на «Личный кабинет»

import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from urls import BASE_URL, LOGIN_PAGE

@pytest.mark.usefixtures("driver", "wait")
class TestNavigationToLogin:

    def test_navigate_to_login_from_main_page(self, driver, wait):
        # 1. Открытие главной страницы
        driver.get(BASE_URL)

        # 2. Клик по кнопке "Личный Кабинет"
        account_button = wait.until(
            EC.element_to_be_clickable(TestLocators.ACCOUNT_BUTTON)
        )
        account_button.click()

        # 3. Ожидание перехода на страницу логина
        wait.until(EC.url_contains(LOGIN_PAGE))

        # 4. Проверка URL
        assert LOGIN_PAGE in driver.current_url, (
            f"Ожидался переход на {LOGIN_PAGE}, но текущий URL: {driver.current_url}"
        )
