import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages import globals


create_campaign = (By.CSS_SELECTOR, '#main-nav li:nth-of-type(5) i')
video_campaign  = (By.CSS_SELECTOR, 'a.icon-facetime-video')

advertiser_form_dropdown = (By.CSS_SELECTOR, '#form_advertiser_id_chosen>a')
advertiser_form_input    = (By.CSS_SELECTOR, '#form_advertiser_id_chosen input')
next_button              = (By.ID, 'finish')

campaign_type_dropdown = (By.CSS_SELECTOR, '#form_video_type_chosen>a')
campaign_type_input    = (By.CSS_SELECTOR, '#form_video_type_chosen input')

tag_url      = (By.ID, 'form_vast_tag')
video_height = (By.ID, 'form_video_height')
video_width  = (By.ID, 'form_video_width')
video_length = (By.ID, 'form_video_length')

campaign_name = (By.ID, 'form_title')
ad_title      = (By.ID, 'form_ad_title')

budget_unit_dropdown = (By.CSS_SELECTOR, '#form_budget_unit_chosen>a')
budget_unit_input    = (By.CSS_SELECTOR, '#form_budget_unit_chosen input')

currency_dropdown   = (By.CSS_SELECTOR, '#form_currency_chosen>a')
currency_input      = (By.CSS_SELECTOR, '#form_currency_chosen input')
add_payout_button   = (By.ID, 'addPayoutButton')
payout_location     = (By.CSS_SELECTOR, '#form_payout_geo_ids_0____chosen input')
payout_amount_left  = (By.NAME, 'payout_sourceAmount_left[]')
payout_amount_right = (By.NAME, 'payout_sourceAmount_right[]')

device_dropdown      = (By.CSS_SELECTOR, '#form_tg_Device_chosen>a')
device_input         = (By.CSS_SELECTOR, '#form_tg_Device_chosen input')
category             = (By.CSS_SELECTOR, '#form_tg_Category___chosen input')
incent_dropdown      = (By.CSS_SELECTOR, '#form_tg_Incent_chosen>a')
incent_input         = (By.CSS_SELECTOR, '#form_tg_Incent_chosen input')
payout_type_dropdown = (By.CSS_SELECTOR, '#form_tg_Payout_Type_chosen>a')
payout_type_input    = (By.CSS_SELECTOR, '#form_tg_Payout_Type_chosen input')
property_type        = (By.CSS_SELECTOR, '#form_tg_Property___chosen input')

created_campaign_table = (By.ID, 'mainTb')

def move_to_next_campaign_creation_form():
    time.sleep(1)
    globals.driver.find_element(*next_button).click()

def create_video_campaign():
    globals.driver.find_element(*create_campaign).click()
    globals.driver.find_element(*video_campaign).click()

def choose_advertiser(name):
    globals.driver.find_element(*advertiser_form_dropdown).click()
    globals.driver.find_element(*advertiser_form_input).send_keys(name)
    globals.driver.find_element(*advertiser_form_input).send_keys(Keys.ENTER)
    globals.driver.find_element(*next_button).click()

def select_campaign_type(name):
    globals.driver.find_element(*campaign_type_dropdown).click()
    globals.driver.find_element(*campaign_type_input).send_keys(name)
    globals.driver.find_element(*campaign_type_input).send_keys(Keys.ENTER)
    globals.driver.find_element(*next_button).click()

def fill_video_details(details):
    globals.driver.find_element(*tag_url).send_keys(details['tag_url'])
    globals.driver.find_element(*video_height).send_keys(details['video_height'])
    globals.driver.find_element(*video_width).send_keys(details['video_width'])
    globals.driver.find_element(*video_length).send_keys(details['video_length'])
    globals.driver.find_element(*next_button).click()

def fill_campaign_details(details):
    globals.driver.find_element(*campaign_name).send_keys(details['name'])
    globals.driver.find_element(*ad_title).send_keys(details['ad_title'])
    globals.driver.find_element(*next_button).click()

def select_budget_unit(budget_type):
    globals.driver.find_element(*budget_unit_dropdown).click()
    globals.driver.find_element(*budget_unit_input).send_keys(budget_type)
    globals.driver.find_element(*budget_unit_input).send_keys(Keys.ENTER)
    globals.driver.find_element(*next_button).click()

def select_currency_and_payout(details):
    globals.driver.find_element(*currency_dropdown).click()
    globals.driver.find_element(*currency_input).send_keys(details['currency'])
    globals.driver.find_element(*currency_input).send_keys(Keys.ENTER)

    globals.driver.find_element(*add_payout_button).click()
    globals.driver.find_element(*payout_location).send_keys(details['payout_location'])
    globals.driver.find_element(*payout_amount_right).send_keys(details['payout_amount_right'])
    globals.driver.find_element(*payout_amount_left).send_keys(details['payout_amount_left'])
    globals.driver.find_element(*next_button).click()

def select_device_and_payout_type(details):
    globals.driver.find_element(*device_dropdown).click()
    globals.driver.find_element(*device_input).send_keys(details['device'])
    globals.driver.find_element(*device_input).send_keys(Keys.ENTER)

    globals.driver.find_element(*category).send_keys(details['category'])
    globals.driver.find_element(*category).send_keys(Keys.ENTER)

    globals.driver.find_element(*incent_dropdown).click()
    globals.driver.find_element(*incent_input).send_keys(details['incent'])
    globals.driver.find_element(*incent_input).send_keys(Keys.ENTER)

    globals.driver.find_element(*payout_type_dropdown).click()
    globals.driver.find_element(*payout_type_input).send_keys(details['payout_type'])
    globals.driver.find_element(*payout_type_input).send_keys(Keys.ENTER)

    globals.driver.find_element(*property_type).send_keys(details['property_type'])
    globals.driver.find_element(*property_type).send_keys(Keys.ENTER)
    globals.driver.find_element(*next_button).click()
    time.sleep(10)

def verify_campaign_created():
    presence = globals.driver.find_element(*created_campaign_table).is_displayed()
    assert(presence == True)

