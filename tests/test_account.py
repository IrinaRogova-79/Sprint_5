import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators, AccountPageLocators
from data import Urls
import helpers

class TestAccount:
    
    @pytest.fixture(autouse=True)
    def login_user(self, driver):
        """Логиним пользователя перед тестами"""
        # Регистрация
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
        
        # Логинимся
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(self.test_email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(self.test_password)
        driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
        
        # Ждем успешного входа (переход на главную)
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Urls.MAIN_PAGE)
        )
        
        # Убираем time.sleep(1) - заменяем на явное ожидание
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT)
        )
        
        yield
    
    def test_go_to_personal_account(self, driver):
        """Переход в личный кабинет"""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        assert "/account/profile" in driver.current_url
    
    def test_go_to_constructor_from_account(self, driver):
        """Переход из личного кабинета в конструктор по кнопке «Конструктор»"""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Urls.MAIN_PAGE)
        )
        assert driver.current_url == Urls.MAIN_PAGE
    
    def test_go_to_main_page_by_logo(self, driver):
        """Переход из личного кабинета на главную по клику на логотип"""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        
        logo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        )
        logo.click()
        
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Urls.MAIN_PAGE)
        )
        assert driver.current_url == Urls.MAIN_PAGE
    
    def test_logout_from_account(self, driver):
        """Выход из аккаунта"""
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()
        
        WebDriverWait(driver, 10).until(
            EC.url_to_be(Urls.LOGIN_PAGE)
        )
        assert driver.current_url == Urls.LOGIN_PAGE