import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en')


@pytest.fixture(scope="function")
def language_cmd(request):
    language = request.config.getoption("language")
    language = None

