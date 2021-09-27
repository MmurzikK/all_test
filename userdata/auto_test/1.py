from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from all_base_test import All_base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class res():
    base_url = All_base.base_url
    #capabilities = {
    #    "browserName": "firefox",
    #    "browserVersion": "92.0",
    #    "selenoid:options": {
    #        "enableVNC": True,
    #        "enableVideo": False
    #    }
    #}    
    #driver = webdriver.Remote(command_executor='http://172.20.96.221:4444/wd/hub',
    #desired_capabilities= capabilities)
    #new_catalog = All_base().test_catalog()  
    driver = webdriver.Firefox()

    def close_modal_city(self):
        base = {'close': 'div.h3__subtext a.city-modal__close'}
        close_button =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, base['close'])))
        close_button.click() 

    def test_price_in_busket(self):
        self.close_modal_city()
        t =1

res().test_price_in_busket()            