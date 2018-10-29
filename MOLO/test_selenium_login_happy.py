import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import date, datetime, timedelta
from random import randint
#
from selenium_dip_consent_page import DipConsentPage
from selenium_dip_calculator_page import DipCalcPage
from selenium_dip_user_data_page import DipUDataPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

@pytest.fixture
def applicant(key):
    # Birth date calculator
    original_dob = date(1960, 6, 25)
    insertion_date = date(2017, 3, 25)
    d = (datetime.now().date() - insertion_date) + original_dob + timedelta(days=1)
    APPLICANT_DOB = d.strftime('%d/%m/%Y')

    # Applicant data
    applicant = {
        'title':'mr',
        'first_name':'Jonathan',
        'middle_name':'Middle',
        'last_name':'Frafer',
        'phone':'+44 161 4521 254',
        'address':'60 Westfield Road, Barton-Upon-Humber, DN18',
        'email': f'vasily.medved{randint(11111,99999)}@djangostars.com',
        'password': 'qqweqqwe',
        'birth_date': APPLICANT_DOB
    }
    return applicant.get(key)

def test_create_new_user(browser):
    # 1. Open {server}
    page = DipCalcPage(browser, 'https://molo:lambda@dev.app.molofinance.com/calculator/')
    # Must reopen the page again since Selenium have no normal ability to do basic auth, and MOLO brakes when opened with creds in URL
    # see 'https://github.com/w3c/webdriver/issues/385'
    browser.get("https://dev.app.molofinance.com/calculator/")

    # assert defaults
    page.income_input.click()
    assert page.income_input.get_attribute("value") == '60,000'
    assert page.rent_input.get_attribute("value") == '1,100'
    assert page.property_value_input.get_attribute("value") == '250,000'
    assert page.desired_loan_amount_input.get_attribute("value") == '200,000'
    # test starts here

    # go to user data page
    page.submit_button.click()
    page = DipUDataPage(browser)
    assert page.tell_us.text == 'TELL US A BIT ABOUT YOURSELF'
    page.mr_choise.click()
    if applicant('title') == 'mr':
        page.mr_choise_mr.click()
        sleep(1)
    page.first_name_input.send_keys(applicant('first_name'))
    page.first_name_input.click()
    page.last_name_input.send_keys(applicant('last_name'))
    page.phone_input.send_keys(applicant('phone'))
    page.birth_date_input.send_keys(applicant('birth_date'))

    # address is a big deal
    page.address_input.click()
    page.address_input.send_keys(applicant('address'))
    sleep(1) #TBD refactor to avoid explicit wait
    browser.switch_to.active_element.send_keys(Keys.DOWN)
    browser.switch_to.active_element.send_keys(Keys.ENTER)
    #
    page.email_input.send_keys(applicant('email'))
    page.password_input.send_keys(applicant('password'))

    # go to checkboxes page
    page.submit_button.click()
    page = DipConsentPage(browser)
    browser.find_element_by_xpath('//input[@data-test="consents-dip_common"]').click()
    browser.find_element_by_xpath('//input[@data-test="consents-marketing"]').click()
    page.soft_credit_check_checkbox.click()
    page.privacy_policy_checkbox.click()
    page.submit_button.click()
    sleep(3)
    assert browser.url == "https://dev.app.molofinance.com/almost"


    '''page = DipConsentPage(browser)
    page.submit_button.click()
    assert len(page.required_warning) == 11
    page.uk_resident_checkbox.check()
    page.no_bankrupt_checkbox.check()
    page.property_england_checkbox.check()
    page.personal_guarantee_checkbox.check()
    page.investment_purposes_checkbox.check()
    page.other_mortgages_checkbox.check()
    page.no_consumer_btl_checkbox.check()
    page.no_hmo_properties_checkbox.check()
    page.single_applicant_checkbox.check()
    page.soft_credit_check_checkbox.check()
    page.privacy_policy_checkbox.check()
    page.submit_button.click()
    sleep(3)
    assert browser.url == "https://dev.app.molofinance.com/almost"
    # page = DipAlmostPage
    # assert page.continue_button_visible is True
    assert browser.find_by_xpath('//*[@data-test="dip-email-verified-continue-submit"]').visible is True'''

    sleep(10)
    #browser.close()