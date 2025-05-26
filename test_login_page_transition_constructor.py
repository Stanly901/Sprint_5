from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_constructor_navigation(driver, wait, base_url):

    # 1. Переход на страницу логина
    driver.get(f"{base_url}/login")

    # 2. Клик по ссылке "Конструктор"
    constructor_link = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Конструктор']")
        )
    )
    constructor_link.click()

    # 3. Проверка перехода на главную страницу
    wait.until(
        EC.url_to_be(f"{base_url}/")
    )