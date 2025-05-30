# Переход между разделами: Булки, Соусы, Начинки

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from locators import TestLocators
from urls import BASE_URL
from test_data import sections

@pytest.mark.usefixtures("driver", "wait")
def test_section_navigation(driver, wait):
    # 1. Открываем главную страницу
    driver.get(BASE_URL)

    for section in sections:
        # 2. Ожидаем кликабельность таба
        section_element = wait.until(
            EC.element_to_be_clickable(TestLocators.tab_by_name(section))
        )

        # Скроллим к табу, чтобы он был видим
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", section_element)
        wait.until(EC.visibility_of(section_element))

        try:
            section_element.click()
        except ElementClickInterceptedException:
            # Если стандартный клик заблокирован, кликаем через JS
            driver.execute_script("arguments[0].click();", section_element)

        # 3. Проверка: выбранный раздел стал активным
        active_section = wait.until(
            EC.presence_of_element_located(TestLocators.active_tab_by_name(section))
        )
        assert active_section is not None, f"Раздел '{section}' не стал активным"
