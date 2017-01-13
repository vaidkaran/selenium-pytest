from selenium import webdriver
from selenium.webdriver.common.by import By
from pages import globals


username = (By.NAME, 'username')
password = (By.NAME, 'password')
submit   = (By.XPATH, 'html/body/div[1]/div/div/div[2]/div/div/div[1]/form/button')

def login_with(username_, password_):
    globals.driver.find_element(*username).send_keys(username_)
    globals.driver.find_element(*password).send_keys(password_)
    globals.driver.find_element(*submit).click()




