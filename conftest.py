from selenium import webdriver
from selenium.webdriver.chrome.options import Options as C_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from pathlib import Path
import pytest
import json

@pytest.fixture
def stepik_creds():
    """Считывание данных для авторизации на stepik из отдельного файла."""
    path = Path('creds.json')
    creds = json.loads(path.read_text())
    return creds['login'], creds['password']

def pytest_addoption(parser):
    """Добавление параметров запуска."""
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox") # Выбор браузера
    parser.addoption('--language', action='store', default='en',
                     help="Choose language") # Выбор языка

@pytest.fixture(scope="function")
def browser(request):
    """Запуск выбранного браузера с параметрами и закрытие по окончанию теста."""
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    browser = None
    if browser_name == "chrome":
        print("\nStart chrome browser for test...")
        if language:
            options = C_Options()
            options.add_experimental_option('prefs',
                                            {'intl.accept_languages': language})
            print(f"\nLanguage: {language}")
            browser = webdriver.Chrome(options=options)
        else:
            browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nStart firefox browser for test...")
        if language:
            options = FF_Options()
            options.set_preference("intl.accept_languages", language)
            print(f"\nLanguage: {language}")
            browser = webdriver.Firefox(options=options)
        else:
            browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nQuit browser...")
    browser.quit()


