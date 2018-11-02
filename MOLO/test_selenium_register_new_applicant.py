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


def explicit_wait(element, browser=browser, time=10):
    WebDriverWait(browser, time).until(
        EC.visibility_of(element)
    )


def molo_address(browser, element, value):
    # There are no simple way to check if react-autosuggest field is populated with value
    explicit_wait(element)
    element.click()
    element.send_keys(value)
    sleep(1.5)
    browser.switch_to.active_element.send_keys(Keys.DOWN)
    sleep(1)
    browser.switch_to.active_element.send_keys(Keys.ENTER)


@pytest.mark.skip
def test_create_new_user(browser, applicant):
    # TBD get rid of this
    global URL, CREDS
    # 1. Open {server} and go to default calculator page
    page = DipCalcPage(browser, f'https://{CREDS}@{URL}/calculator/')
    # Must reopen the page again since Selenium have no normal ability to do basic auth, and MOLO brakes when opened with creds in URL
    # see 'https://github.com/w3c/webdriver/issues/385'
    explicit_wait(page.desired_loan_amount_input)
    browser.get(f'https://{URL}/calculator/')

    # No way to determine if API call is finished, so inserted sleep
    sleep(3)

    # Calculator page
    explicit_wait(page.submit_button)
    explicit_wait(page.desired_loan_amount_input)
    assert page.income_input.get_attribute("value") == '60,000'
    assert page.rent_input.get_attribute("value") == '1,200'
    assert page.property_value_input.get_attribute("value") == '250,000'
    assert page.desired_loan_amount_input.get_attribute("value") == '150,000'

    # User data page
    page.submit_button.click()
    page = DipUDataPage(browser)
    explicit_wait(page.tell_us)
    page.mr_choise.click()
    explicit_wait(page.mr_choise)
    page.mr_choise_mr.click()
    sleep(1)
    #
    page.first_name_input.send_keys(applicant['first_name'])
    page.first_name_input.click()
    page.last_name_input.send_keys(applicant['last_name'])
    page.phone_input.send_keys(applicant['phone'])
    page.birth_date_input.send_keys(applicant['birth_date'])
    molo_address(browser, page.address_input, applicant['register_address'])
    page.email_input.send_keys(applicant['email'])
    page.password_input.send_keys(applicant['password'])

    # Consent page
    page.submit_button.click()
    page = DipConsentPage(browser)
    browser.find_element_by_xpath('//input[@data-test="consents-dip_common"]').click()
    browser.find_element_by_xpath('//input[@data-test="consents-marketing"]').click()
    page.soft_credit_check_checkbox.click()
    page.privacy_policy_checkbox.click()
    page.submit_button.click()

    # Almost page
    explicit_wait(browser.find_element_by_xpath('//h2[text()="Your quote is on its way!"]'))
    assert ('almost' in browser.current_url) == True
    sleep(10)


# @pytest.mark.skip
def test_login_and_be_happy_registered_user(browser, applicant):
    # time to activate user account manually. To be deleted
    global URL, CREDS
    #
    page = LoginPage(browser, f'https://{CREDS}@{URL}/login/')
    # Must reopen the page again since Selenium have no normal ability to do basic auth, and MOLO brakes when opened with creds in URL
    # see 'https://github.com/w3c/webdriver/issues/385'
    explicit_wait(page.login_button)
    browser.get(f'https://{URL}/login/')
    assert ('login' in browser.current_url) == True
    explicit_wait(page.login_button)
    assert (page.login_button.is_displayed() == True)
    page.email_input.send_keys('vasily.medved+84363@djangostars.com')
    page.password_input.send_keys(applicant['password'])
    page.login_button.click()
    sleep(5)

    # Dashboard page
    page = HeaderPage(browser)
    explicit_wait(page.your_account_menu)
    page.your_account_menu.click()
    explicit_wait(page.calculator_menu)
    page.calculator_menu.click()

    # Calculator page
    assert ('calculator' in browser.current_url) == True
    page = DipCalcPage(browser)
    explicit_wait(page.products_table)
    explicit_wait(page.submit_button,time=60)
    page.submit_button.click()

    # Congrats page
    page = CongratsPage(browser)
    explicit_wait(page.submit_button,60)
    assert ('congrats' in browser.current_url) == True
    page.submit_button.click()

    # Address history verification page (optional)
    page = PropertyPage(browser)
    sleep(3)
    if ('address-history-verification' in browser.current_url) == True:
        explicit_wait(page.history_property)
        molo_address(browser, page.history_property, applicant['history_property_address'])
        explicit_wait(page.history_page_submit_button)
        page.history_page_submit_button.click()

    # Property details page
    # Sorry for the sleeps, I honestly tried.
    page = PropertyPage(browser)
    explicit_wait(page.address_input)
    molo_address(browser, page.address_input, applicant['property_address'])
    page.built_year_input.send_keys(applicant['year_built'])
    page.property_price_input.send_keys(applicant['purchase_price'])
    page.monthly_rent_input.send_keys(applicant['monthly_rent'])
    page.bedroooms_qty_input.send_keys(applicant['bedrooms'])
    # the sleeps looks like optimal solution for race conditions between browser and selenium when working with custom MaterialUI React elements
    # see also https://blog.codeship.com/get-selenium-to-wait-for-page-load/
    sleep(1)
    ActionChains(browser).move_to_element(page.property_type_dropdown).click(page.property_type_dropdown).perform()
    sleep(0.5)
    explicit_wait(page.property_type_mid_terrace_choice)
    page.property_type_mid_terrace_choice.click()
    sleep(1)
    ActionChains(browser).move_to_element(page.property_construction_material_dropdown).click(
        page.property_construction_material_dropdown).perform()
    sleep(0.5)
    explicit_wait(page.property_construction_material_choise)
    page.property_construction_material_choise.click()
    sleep(1)
    page.hmo_no_radiobutton.click()
    page.exlocal_no_radiobutton.click()
    explicit_wait(page.continue_button)
    page.continue_button.click()

    # Select product page
    page = ProductSelectorPage(browser)
    explicit_wait(page.product_list_table)
    assert ('select-product' in browser.current_url) == True
    sleep(100)




