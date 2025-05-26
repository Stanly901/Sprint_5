from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_section_navigation(driver, wait, base_url, sections):

    # 1. Открываем главную страницу
    driver.get(base_url)

    # 2. Проверяем навигацию по всем разделам
    for section in sections:
        # Находим и кликаем на раздел
        section_element = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[contains(@class, 'tab_tab__')]//span[text()='{section}']/..")
            )
        )
        section_element.click()

        # Проверяем, что раздел активен
        active_section = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, f"//div[contains(@class, 'tab_tab_type_current__')]//span[text()='{section}']")
            )
        )
        assert active_section is not None, f"Раздел '{section}' не стал активным"