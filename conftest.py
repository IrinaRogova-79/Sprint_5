import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")

@pytest.fixture
def driver(request):
    """Фикстура для инициализации драйвера"""
    browser = request.config.getoption("--browser")
    
    if browser == "chrome":
        options = ChromeOptions()
        # options.add_argument("--headless")  # Раскомментировать для headless режима
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        # options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Browser {browser} not supported")
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def registered_user(driver, helpers):
    """Фикстура для создания зарегистрированного пользователя"""
    driver.get(Urls.REGISTER_PAGE)
    
    name = helpers.generate_name()
    email = helpers.generate_unique_email()
    password = helpers.generate_valid_password()
    
    from locators import AuthPageLocators
    
    driver.find_element(*AuthPageLocators.NAME_INPUT).send_keys(name)
    driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthPageLocators.REGISTER_BUTTON).click()
    
    return {"name": name, "email": email, "password": password}