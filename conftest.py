import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options #открытие браузера в управляемом режиме

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless') # открытии браузера НЕ в визуальном режиме
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.close()