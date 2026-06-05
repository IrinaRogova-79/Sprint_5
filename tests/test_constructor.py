import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators
from data import Urls

class TestConstructor:
    
    @pytest.fixture(autouse=True)
    def open_main_page(self, driver):
        """Открываем главную страницу перед каждым тестом"""
        driver.get(Urls.MAIN_PAGE)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.BUNS_SECTION)
        )
        yield
    
    def test_go_to_sauces_section(self, driver):
        """Переход к разделу «Соусы»"""
        sauces = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
        )
        sauces.click()
        
        # Проверяем, что раздел стал активным
        active_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc"))
        )
        active_text = active_section.find_element(By.TAG_NAME, "span").text
        
        assert "Соусы" in active_text
    
    def test_go_to_fillings_section(self, driver):
        """Переход к разделу «Начинки»"""
        fillings = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.FILLINGS_SECTION)
        )
        fillings.click()
        
        active_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc"))
        )
        active_text = active_section.find_element(By.TAG_NAME, "span").text
        
        assert "Начинки" in active_text
    
    def test_go_to_buns_section(self, driver):
        """Переход к разделу «Булки»"""
        # Сначала переходим в раздел "Соусы"
        sauces = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
        )
        sauces.click()
        
        # Ждем активации раздела "Соусы"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc"))
        )
        
        # Затем возвращаемся к "Булкам"
        buns = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.BUNS_SECTION)
        )
        buns.click()
        
        # Проверяем, что Булки стали активными
        active_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".tab_tab_type_current__2BEPc"))
        )
        active_text = active_section.find_element(By.TAG_NAME, "span").text
        
        assert "Булки" in active_text