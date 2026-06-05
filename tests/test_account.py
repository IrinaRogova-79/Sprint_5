import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AccountPageLocators
from data import Urls

class TestAccount:
    
    def test_go_to_personal_account(self, logged_in_user):
        """Переход в личный кабинет"""
        driver = logged_in_user
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        
        WebDriverWait(driver, 10).until(
            EC.url_contains("/account/profile")
        )
        assert "/account/profile" in driver.current_url
    
    def test_go_to_constructor_from_account(self, logged_in_user):
        """Переход из личного кабинета в конструктор по кнопке «Конструктор»"""
        driver = logged_in_user
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert driver.current_url == Urls.MAIN_PAGE
    
    def test_go_to_main_page_by_logo(self, logged_in_user):
        """Переход из личного кабинета на главную по клику на логотип"""
        driver = logged_in_user
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        
        logo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        )
        logo.click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
        assert driver.current_url == Urls.MAIN_PAGE
    
    def test_logout_from_account(self, logged_in_user):
        """Выход из аккаунта"""
        driver = logged_in_user
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
        assert driver.current_url == Urls.LOGIN_PAGE