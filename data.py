class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru"
    MAIN_PAGE = f"{BASE_URL}/"
    LOGIN_PAGE = f"{BASE_URL}/login"
    REGISTER_PAGE = f"{BASE_URL}/register"
    FORGOT_PASSWORD_PAGE = f"{BASE_URL}/forgot-password"
    ACCOUNT_PAGE = f"{BASE_URL}/account/profile"
    RESET_PASSWORD_PAGE = f"{BASE_URL}/reset-password"  # Добавлено

class UserData:
    NAME = "Тестовый Пользователь"
    VALID_PASSWORD = "123456"
    INVALID_PASSWORD = "12345"  # Меньше 6 символов