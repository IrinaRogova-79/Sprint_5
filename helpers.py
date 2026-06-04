import random
import string
from faker import Faker

fake = Faker('ru_RU')

def generate_unique_email():
    """
    Генерирует уникальный email в формате имя_фамилия_когорта_рандом@домен
    Пример: ivan_petrov_123_456@yandex.ru
    """
    first_name = fake.first_name().lower()
    last_name = fake.last_name().lower()
    cohort = random.randint(100, 999)
    random_digits = random.randint(100, 999)
    
    email = f"{first_name}_{last_name}_{cohort}_{random_digits}@yandex.ru"
    return email

def generate_name():
    """Генерирует случайное имя"""
    return fake.first_name()

def generate_valid_password():
    """Генерирует валидный пароль (6+ символов)"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(6, 12)))

def generate_invalid_password():
    """Генерирует невалидный пароль (менее 6 символов)"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 5)))