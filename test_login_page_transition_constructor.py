# Переход по клику на «Конструктор».

import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
from urls import BASE_URL, LOGIN_PAGE

@pytest.mark.usefixtures("driver", "wait")
class TestNavigation:

    def test_navigation_from_login_to_constructor(self, driver, wait):
        # 1. Переход на страницу логина
        driver.get(f"{BASE_URL}{LOGIN_PAGE}")

        # 2. Клик по ссылке "Конструктор" в шапке
        constructor_link = wait.until(
            EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_LINK)
        )
        constructor_link.click()

        # 3. Ожидание появления заголовка "Соберите бургер"
        burger_header = wait.until(
            EC.visibility_of_element_located(TestLocators.BURGER_HEADER)
        )

        # 4. Проверка: заголовок конструктора отображается
        assert burger_header.is_displayed(), "Заголовок конструктора не отображается — переход не удался"


