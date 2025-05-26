from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_logo_navigation(driver, wait, base_url):

    # 1. Переходим на страницу авторизации
    driver.get(f"{base_url}/login")

    # 2. Кликаем по логотипу
    logo = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]")
        )
    )
    logo.click()

    # 3. Проверяем переход на главную страницу
    wait.until(
        EC.url_to_be(f"{base_url}/")
    )