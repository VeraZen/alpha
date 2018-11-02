from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
#

import pytest
from time import sleep
from datetime import date, datetime, timedelta
from random import randint
#
from selenium_header_page import HeaderPage
from selenium_dip_consent_page import DipConsentPage
from selenium_dip_calculator_page import DipCalcPage
from selenium_dip_user_data_page import DipUDataPage
from selenium_login_page import LoginPage
from selenium_dashboard_page import DashboardPage
from selenium_congrats_page import CongratsPage
from selenium_property_page import PropertyPage
from selenium_product_selector_page import ProductSelectorPage
from selenium_product_terms_page import ProductTerms

URL = 'dev.app.molofinance.com'
CREDS = 'molo:lambda'

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.implicitly_wait(20)
    return driver


@pytest.fixture(scope="module")
def applicant():
    # Birth date calculator
    original_dob = date(1960, 6, 25)
    insertion_date = date(2017, 3, 25)
    d = (datetime.now().date() - insertion_date) + original_dob + timedelta(days=1)
    APPLICANT_DOB = d.strftime('%d/%m/%Y')

    # Applicant data
    applicant = {
        'title': 'mr',
        'first_name': 'Jonathan',
        'middle_name': 'Middle',
        'last_name': 'Frafer',
        'phone': '+44 161 4521 254',
        'register_address': '60 Westfield Road, Barton-Upon-Humber, DN18',
        'history_property_address': '34 Abbots Road, Abbots Langley, WD5',
        'property_address': '2 Fiars Terrace, Stafford, ST17',
        'year_built': '1900',
        'purchase_price': '110000',
        'monthly_rent': '1100',
        'property_type': 'House - Mid terrace',
        'bedrooms': '2',
        'is_ex_local': 'NO',
        'is_HMO': 'NO',
        'loan_type': 'new',
        'loan_years': '25',
        'loan_amount': '80000',
        'source_of_deposit': 'Savings',
        'email': f'vasily.medved+{randint(11111,99999)}@djangostars.com',
        'password': 'qqweqqwe',
        'birth_date': APPLICANT_DOB
    }
    return applicant


def explicit_wait(element, browser=browser, time=10, dumb_sleep=0):
    sleep(dumb_sleep)
    WebDriverWait(browser, time).until(
        EC.visibility_of(element)
    )


def molo_address(browser, element, value):
    explicit_wait(element)
    element.click()
    element.send_keys(value)
    sleep(1.5)
    browser.switch_to.active_element.send_keys(Keys.DOWN)
    sleep(1)
    browser.switch_to.active_element.send_keys(Keys.ENTER)

def molo_clear_input(element, browser=browser):
    sleep(0.5)
    element.click()
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.DELETE)
    sleep(0.5)




# @pytest.mark.skip
def test_login_and_be_happy_registered_user(browser, applicant):
    # TBD get rid of this
    global URL, CREDS
    #
    page = LoginPage(browser, f'https://{CREDS}@{URL}/login/')
    # Must reopen the page again since Selenium have no normal ability to do basic auth, and MOLO brakes when opened with creds in URL
    # see 'https://github.com/w3c/webdriver/issues/385'
    explicit_wait(page.login_button)
    browser.get(f'https://{URL}/login/')
    explicit_wait(page.login_button)
    page.email_input.send_keys('vasily.medved+84363@djangostars.com')
    page.password_input.send_keys(applicant['password'])
    page.login_button.click()
    sleep(5)
    browser.get(f'https://dev.app.molofinance.com/complete-offer/1000001240/select-product')
    sleep(5)

    # Product selection page
    page = ProductSelectorPage(browser)
    explicit_wait(page.product_list_table)
    assert ('select-product' in browser.current_url) == True
    explicit_wait(page.loan_type_button)
    page.loan_type_button.click()
    page.user_loan_amount_input.click()
    molo_clear_input(page.user_loan_amount_input)
    page.user_loan_amount_input.send_keys(applicant['loan_amount'])
    page.product_checkbox.click()
    explicit_wait(page.submit_button)
    page.submit_button.click()
    explicit_wait(browser.find_by_xpath('//div[text()="X"]'))
    page.submit_button.click()

    # Product terms page
    page = ProductTerms(browser)
    explicit_wait(page.submit_button)
    page.allow_fraud_checkbox.click()
    page.automated_assessment_checkbox.click()
    page.full_credit_search_checkbox.click()
    page.mortgage_conditions_checkbox.click()
    page.submit_button.click()
    print('voila')
    sleep(1000)






