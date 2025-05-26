from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_personal_account_navigation(driver, wait, base_url):

    # 1. Переходим на главную страницу
    driver.get(base_url)

    # 2. Кликаем по кнопке "Личный Кабинет"
    account_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Личный Кабинет']")
        )
    )
    account_button.click()

    # 3. Проверяем переход на страницу авторизации
    wait.until(
        EC.url_contains("/login")
    )