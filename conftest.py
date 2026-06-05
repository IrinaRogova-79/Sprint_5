import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AuthPageLocators
from data import Urls
import helpers

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")

@pytest.fixture
def driver(request):
    """Фикстура для инициализации драйвера"""
    browser = request.config.getoption("--browser")
    
    if browser == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Browser {browser} not supported")
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_user(driver):
    """Фикстура для создания и авторизации пользователя"""
    driver.get(Urls.REGISTER_PAGE)
    
    test_email = helpers.generate_unique_email()
    test_password = helpers.generate_valid_password()
    test_name = helpers.generate_name()
    
    # Регистрация
    driver.find_element(*AuthPageLocators.NAME_INPUT).send_keys(test_name)
    driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(test_email)
    driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(test_password)
    driver.find_element(*AuthPageLocators.REGISTER_BUTTON).click()
    
    # Ждем перехода на страницу логина
    WebDriverWait(driver, 10).until(EC.url_to_be(Urls.LOGIN_PAGE))
    
    # Логинимся
    driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(test_email)
    driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(test_password)
    driver.find_element(*AuthPageLocators.LOGIN_BUTTON).click()
    
    # Ждем успешного входа
    WebDriverWait(driver, 10).until(EC.url_to_be(Urls.MAIN_PAGE))
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[text()='Личный Кабинет']"))
    )
    
    yield driver