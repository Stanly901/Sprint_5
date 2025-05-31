# Переход по клику на «Логотип».

import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from urls import BASE_URL, LOGIN_PAGE

@pytest.mark.usefixtures("driver", "wait")
class TestNavigationFromLoginPage:

    def test_logo_navigation_from_login_page(self, driver, wait):
        # 1. Переход на страницу авторизации
        driver.get(f"{BASE_URL}{LOGIN_PAGE}")

        # 2. Клик по логотипу
        logo = wait.until(
            EC.element_to_be_clickable(TestLocators.LOGO)
        )
        logo.click()

        # 3. Ожидание отображения заголовка конструктора
        burger_header = wait.until(
            EC.visibility_of_element_located(TestLocators.BURGER_HEADER)
        )

        # 4. Проверка: заголовок конструктора отображается
        assert burger_header.is_displayed(), "Заголовок конструктора не отображается — переход по логотипу не сработал"


