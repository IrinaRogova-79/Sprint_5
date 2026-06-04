import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators
from data import Urls
import helpers

class TestLogin:
    
    @pytest.fixture(autouse=True)
    def create_test_user(self, driver):
        """Создаем тестового пользователя для входа"""
        driver.get(Urls.REGISTER_PAGE)
        
        self.test_email = helpers.generate_unique_email()
        self.test_password = helpers.generate_valid_password()
        self.test_name = helpers.generate_name()
        
        driver.find_element(*AuthPageLocators.NAME_INPUT).send_keys(self.test_name)
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(self.test_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*AuthPageLocators.REGISTER_BUTTON).click()
        
        # Ждем перехода на страницу логина
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Urls.LOGIN_PAGE)
        )
        
        yield
    
    def test_login_by_main_button(self, driver):
        """Вход по кнопке «Войти в аккаунт» на главной"""
        driver.get(Urls.MAIN_PAGE)
        
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
        
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(self.test_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert driver.current_url == Urls.MAIN_PAGE
    
    def test_login_by_personal_account_button(self, driver):
        """Вход через кнопку «Личный кабинет»"""
        driver.get(Urls.MAIN_PAGE)
        
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
        
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(self.test_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert driver.current_url == Urls.MAIN_PAGE
    
    def test_login_from_registration_page(self, driver):
        """Вход через кнопку в форме регистрации"""
        driver.get(Urls.REGISTER_PAGE)
        
        # Нажимаем на ссылку "Войти" на странице регистрации
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AuthPageLocators.LOGIN_FROM_REGISTER)
        ).click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
        
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(self.test_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert driver.current_url == Urls.MAIN_PAGE
    
    def test_login_from_password_recovery_page(self, driver):
        """Вход через кнопку в форме восстановления пароля"""
        driver.get(Urls.FORGOT_PASSWORD_PAGE)
        
        # Ждем и кликаем на ссылку "Войти" на странице восстановления
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AuthPageLocators.LOGIN_FROM_FORGOT)
        ).click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
        
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(self.test_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert driver.current_url == Urls.MAIN_PAGE