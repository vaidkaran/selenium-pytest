import time
import pytest
from pages import welcome_page
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select



driver = None

def setup_function():
    global driver
    driver = webdriver.Firefox()

def teardown_function():
    global driver
    driver.quit()

def test_google_title():
    global driver
    driver.get('https://dev-admin.woobi.com')
    driver.find_element_by_name('username').send_keys('khanna.vijay@tftus.com')
    driver.find_element_by_name('password').send_keys('Vijay_Woobi@123')
    driver.find_element_by_xpath('html/body/div[1]/div/div/div[2]/div/div/div[1]/form/button').click()
    driver.find_element_by_css_selector('#main-nav li:nth-of-type(5) i').click()
    driver.find_element_by_css_selector('a.icon-facetime-video').click()
    time.sleep(2)

    # Choose advertiser
    driver.find_element_by_css_selector('#form_advertiser_id_chosen>a').click()
    driver.find_element_by_css_selector('#form_advertiser_id_chosen input').send_keys('1595')
    driver.find_element_by_css_selector('#form_advertiser_id_chosen input').send_keys(Keys.ENTER)
    # driver.find_element_by_css_selector('li.active-result').click()
    driver.find_element_by_css_selector('button#finish').click()
    time.sleep(5)

    # select campaign type
    driver.find_element_by_css_selector('#form_video_type_chosen>a').click()
    driver.find_element_by_css_selector('#form_video_type_chosen input').send_keys('Vast tag')
    driver.find_element_by_css_selector('#form_video_type_chosen input').send_keys(Keys.ENTER)
    driver.find_element_by_css_selector('button#finish').click()

    # Fill up video details
    driver.find_element_by_id('form_vast_tag').send_keys('https://ssp.lkqd.net/ad?pid=200&sid=69447&output=vastvpaid&support=html5flash&execution=any&placement=&playinit=auto&volume=100')
    driver.find_element_by_id('form_video_height').send_keys('500')
    driver.find_element_by_id('form_video_width').send_keys('500')
    driver.find_element_by_id('form_video_length').send_keys('50')
    driver.find_element_by_css_selector('button#finish').click()

    # Campaign details
    driver.find_element_by_id('form_title').send_keys('test campaign')
    driver.find_element_by_id('form_ad_title').send_keys('test ad title')
    driver.find_element_by_css_selector('button#finish').click()

    time.sleep(2)
    driver.find_element_by_css_selector('button#finish').click()

    # Budget unit
    driver.find_element_by_css_selector('#form_budget_unit_chosen>a').click()
    driver.find_element_by_css_selector('#form_budget_unit_chosen input').send_keys('No budget')
    driver.find_element_by_css_selector('#form_budget_unit_chosen input').send_keys(Keys.ENTER)
    driver.find_element_by_css_selector('button#finish').click()

    # Currency and Payout
    # time.sleep(50)
    driver.find_element_by_css_selector('#form_currency_chosen>a').click()
    driver.find_element_by_css_selector('#form_currency_chosen input').send_keys('USD')
    driver.find_element_by_css_selector('#form_currency_chosen input').send_keys(Keys.ENTER)
    driver.find_element_by_id('addPayoutButton').click()
    time.sleep(2)

    driver.find_element_by_css_selector('#form_payout_geo_ids_0____chosen input').send_keys('Australia')
    driver.find_element_by_css_selector('#form_payout_geo_ids_0____chosen input').send_keys(Keys.ENTER)
    driver.find_element_by_name('payout_sourceAmount_left[]').send_keys('25')
    driver.find_element_by_name('payout_sourceAmount_right[]').send_keys('0')
    driver.find_element_by_css_selector('button#finish').click()

    # Device and payout type
    driver.find_element_by_css_selector('#form_tg_Device_chosen>a').click()
    driver.find_element_by_css_selector('#form_tg_Device_chosen input').send_keys('Web / All')
    driver.find_element_by_css_selector('#form_tg_Device_chosen input').send_keys(Keys.ENTER)

    driver.find_element_by_css_selector('#form_tg_Category___chosen input').send_keys('Video Web')
    driver.find_element_by_css_selector('#form_tg_Category___chosen input').send_keys('Keys.ENTER')

    driver.find_element_by_css_selector('#form_tg_Incent_chosen>a').click()
    driver.find_element_by_css_selector('#form_tg_Incent_chosen input').send_keys('Incentive')
    driver.find_element_by_css_selector('#form_tg_Incent_chosen input').send_keys(Keys.ENTER)

    driver.find_element_by_css_selector('#form_tg_Payout_Type_chosen>a').click()
    driver.find_element_by_css_selector('#form_tg_Payout_Type_chosen input').send_keys('CPM')
    driver.find_element_by_css_selector('#form_tg_Payout_Type_chosen input').send_keys(Keys.ENTER)

    driver.find_element_by_css_selector('#form_tg_Property___chosen input').send_keys('Free')
    driver.find_element_by_css_selector('#form_tg_Property___chosen input').send_keys(Keys.ENTER)
    driver.find_element_by_css_selector('button#finish').click()

    time.sleep(9)
