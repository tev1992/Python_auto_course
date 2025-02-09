from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def Open(self):
        self.browser.get('https://demoblaze.com')

    def click_galaxy(self):
        click_galaxy = self.browser.find_element(By.XPATH, '//a[text()="Samsung galaxy s6"]')
        click_galaxy.click()

    def click_monitor(self):
        click_monitors = self.browser.find_element(By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]''')
        click_monitors.click()

    def check_products_count(self, count):
        monitors = self.browser.find_elements(By.CSS_SELECTOR, '.card.h-100')
        assert len(monitors) == count  # провека кол-ва элементов