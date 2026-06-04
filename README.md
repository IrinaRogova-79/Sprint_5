# Sprint_5 - Автотесты для Stellar Burgers

## Описание проекта
Автотесты для сервиса Stellar Burgers (https://stellarburgers.education-services.ru/), тестирующие функциональность регистрации, входа, личного кабинета и конструктора.

## Технологии
- Python 3.9+
- Selenium WebDriver
- Pytest
- Google Chrome / Mozilla Firefox

## Установка и запуск
1. Клонировать репозиторий
2. Установить зависимости: `pip install -r requirements.txt`
3. Установить ChromeDriver и GeckoDriver
4. Запустить тесты: `pytest -v`

## Структура проекта
- `conftest.py` - фикстуры для браузеров
- `locators.py` - описание локаторов
- `data.py` - тестовые данные
- `helpers.py` - вспомогательные функции
- `tests/` - директория с тестами
