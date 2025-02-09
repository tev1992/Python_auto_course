import time
from itertools import product
from selenium.webdriver.common.by import By #открытие браузера в визуальном режиме
from pages.homepage import HomePage
from pages.product import ProductPage

def test_open_s6(browser):

    homepage = HomePage(browser)
    homepage.Open()
    homepage.click_galaxy()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')


def test_monitors(browser):
    homepage = HomePage(browser)
    homepage.Open()
    homepage.click_monitor()
    time.sleep(3)
    #monitors = browser.find_elements(By.CSS_SELECTOR, '.card.h-100')
    #assert len(monitors) == 2 #провека кол-ва элементов
    homepage.check_products_count(2)

