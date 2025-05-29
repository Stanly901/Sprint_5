import pytest
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

@pytest.mark.usefixtures("driver", "wait", "base_url")
class TestNavigationFromLogo:

    def test_logo_navigation_from_login_page(self, driver, wait, base_url):
        # 1. Переходим на страницу авторизации
        driver.get(f"{base_url}/login")

        # 2. Кликаем по логотипу на главной странице
        logo = wait.until(
            EC.element_to_be_clickable(TestLocators.LOGO)
        )
        logo.click()

        # 3. Ожидание загрузки элемента на главной странице
        burger_header = wait.until(
            EC.visibility_of_element_located(TestLocators.BURGER_HEADER)
        )

        # 4. Проверка: заголовок конструктора отображается
        assert burger_header.is_displayed(), "Заголовок конструктора не отображается — переход не удался"