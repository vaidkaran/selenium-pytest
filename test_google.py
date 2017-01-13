import time
import pytest
from selenium import webdriver

from pages import login_page
from pages import index_page
from pages import globals


def setup_function():
    globals.driver = webdriver.Firefox()
    globals.driver.implicitly_wait(5)
    globals.driver.get('https://dev-admin.woobi.com')

def teardown_function():
    globals.driver.quit()

def test_create_campaign():
    login_page.login_with('khanna.vijay@tftus.com', 'Vijay_Woobi@123')
    index_page.create_video_campaign()
    index_page.choose_advertiser('1595 - TFT_Test')
    index_page.select_campaign_type('Vast tag')

    video_details = {
        'tag_url'      : 'https : //ssp.lkqd.net/ad?pid=200&sid=69447&output=vastvpaid&support=html5flash&execution=any&placement=&playinit=auto&volume=100',
        'video_height' : '50',
        'video_width'  : '50',
        'video_length' : '5' }
    index_page.fill_video_details(video_details)

    campaign_details = {
        'name'     : 'test campaign',
        'ad_title' : 'test ad title' }
    index_page.fill_campaign_details(campaign_details)

    index_page.move_to_next_campaign_creation_form()
    index_page.select_budget_unit('No budget')

    currency_and_payout_details = {
        'currency'            : 'USD',
        'payout_location'     : 'Australia',
        'payout_amount_left'  : '25',
        'payout_amount_right' : '0' }
    index_page.select_currency_and_payout(currency_and_payout_details)

    device_and_payout_details = {
        'device'        : 'Web / All',
        'category'      : 'Video Web',
        'incent'        : 'Incentive',
        'payout_type'   : 'CPM',
        'property_type' : 'Free' }
    index_page.select_device_and_payout_type(device_and_payout_details)
    index_page.verify_campaign_created()
