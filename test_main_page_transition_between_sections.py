# Переход между разделами: Булки, Соусы, Начинки
import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from locators import TestLocators

@pytest.mark.usefixtures("driver", "wait", "base_url", "sections")
class TestSectionNavigation:

    def test_section_navigation(self, driver, wait, base_url, sections):
        # 1. Открываем главную страницу
        driver.get(base_url)

        for section in sections:
            # 2. Ожидаем кликабельность раздела на главной странице
            section_element = wait.until(
                EC.element_to_be_clickable(TestLocators.tab_by_name(section))
            )

            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", section_element)
            wait.until(EC.visibility_of(section_element))

            try:
                section_element.click()
            except ElementClickInterceptedException:
                time.sleep(1)
                driver.execute_script("arguments[0].click();", section_element)

            # 3. Проверка: раздел активен
            active_section = wait.until(
                EC.presence_of_element_located(TestLocators.active_tab_by_name(section))
            )
            assert active_section is not None, f"Раздел '{section}' не стал активным"