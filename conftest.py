import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    # В переменную user_language передается параметр из командной строки
    user_language = request.config.getoption('language')

    # Инициализируются опции браузера
    options = Options()

    # В опции вебдрайвера передаем параметр из командной строки
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    browser.implicitly_wait(5)
    yield browser
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def pytest_addoption(parser):
    """Опции командной строки.
    В командную строку передается параметр вида '--language="es"'
    По умолчанию передается параметр, включающий английский интерфейс в браузере
    """
    parser.addoption('--language', action='store', default='en', help='Choose language')





# Выбор браузера, пока не готово.

#@pytest.fixture(scope="function")
#def browser(request):
#    browser_name = request.config.getoption("browser_name")
#    browser = None
#    if browser_name == "chrome":
#        print("\nstart chrome browser for test..")
#        browser = webdriver.Chrome()
#    elif browser_name == "firefox":
#        print("\nstart firefox browser for test..")
#        browser = webdriver.Firefox()
#    else:
#        raise pytest.UsageError("--browser_name should be chrome or firefox")
#    yield browser
#    print("\nquit browser..")
#    browser.quit()

