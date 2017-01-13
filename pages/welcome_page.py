from selenium import webdriver
from selenium.webdriver.common.by import By

class WelcomePage:

    paytm_wallet = (By.LINK_TEXT, 'Paytm Wallet')

    def __init__(self, driver):
        self.driver = driver

    def goto_paytm_wallet(self):
        self.find_element(paytm_wallet).click()

