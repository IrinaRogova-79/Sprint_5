from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопки на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    
    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    # Активный раздел - более точный локатор
    ACTIVE_SECTION = (By.CLASS_NAME, "tab_tab_type_current__2BEPc")
    # Альтернативный вариант для поиска активного раздела по родителю
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]//span")

class AuthPageLocators:
    # Форма регистрации
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    
    # Кнопки для входа (более точные локаторы)
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    LOGIN_FROM_REGISTER = (By.XPATH, "//a[text()='Войти']")
    LOGIN_FROM_FORGOT = (By.XPATH, "//a[text()='Войти']")  # Для страницы восстановления
    
    # Ошибки
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")
    
    # Заголовок успешной регистрации
    REGISTRATION_SUCCESS = (By.XPATH, "//h2[text()='Вход']")

class AccountPageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    PROFILE = (By.XPATH, "//a[text()='Профиль']")