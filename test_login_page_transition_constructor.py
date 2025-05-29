# Проверь переход по клику на «Конструктор».

import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

@pytest.mark.usefixtures("driver", "wait", "base_url")
class TestConstructorNavigation:

    def test_navigation_from_login_to_constructor(self, driver, wait, base_url):
        # 1. Переход на страницу логина
        driver.get(f"{base_url}/login")

        # 2. Клик по ссылке "Конструктор" на главной странице
        constructor_link = wait.until(
            EC.element_to_be_clickable(TestLocators.CONSTRUCTOR_LINK)
        )
        constructor_link.click()

        # 3. Ожидание загрузки элемента на главной странице
        burger_header = wait.until(
            EC.visibility_of_element_located(TestLocators.BURGER_HEADER)
        )

        # 4. Проверка: заголовок конструктора отображается
        assert burger_header.is_displayed(), "Заголовок конструктора не отображается — переход не удался"