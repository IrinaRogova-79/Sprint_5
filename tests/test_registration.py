import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthPageLocators, MainPageLocators
from data import Urls
import helpers

class TestRegistration:
    
    def test_successful_registration(self, driver):
        """Тест успешной регистрации"""
        driver.get(Urls.REGISTER_PAGE)
        
        name = helpers.generate_name()
        email = helpers.generate_unique_email()
        password = helpers.generate_valid_password()
        
        driver.find_element(*AuthPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.REGISTER_BUTTON).click()
        
        # После успешной регистрации должен открыться экран входа
        WebDriverWait(driver, 5).until(
            EC.url_to_be(Urls.LOGIN_PAGE)
        )
        
        assert driver.current_url == Urls.LOGIN_PAGE
    
    def test_registration_with_invalid_password(self, driver):
        """Тест регистрации с некорректным паролем (менее 6 символов)"""
        driver.get(Urls.REGISTER_PAGE)
        
        name = helpers.generate_name()
        email = helpers.generate_unique_email()
        password = helpers.generate_invalid_password()
        
        driver.find_element(*AuthPageLocators.NAME_INPUT).send_keys(name)
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.REGISTER_BUTTON).click()
        
        # Проверяем появление ошибки
        error_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(AuthPageLocators.PASSWORD_ERROR)
        )
        
        assert error_element.is_displayed()