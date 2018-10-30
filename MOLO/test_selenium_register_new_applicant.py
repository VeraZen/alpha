import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from datetime import date, datetime, timedelta
from random import randint
#
from selenium_dip_consent_page import DipConsentPage
from selenium_dip_calculator_page import DipCalcPage
from selenium_dip_user_data_page import DipUDataPage
from selenium_login_page import LoginPage
from selenium_dashboard_page import DashboardPage
from selenium_congrats_page import CongratsPage
from selenium_property_page import PropertyPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.implicitly_wait(10)
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
        'title':'mr',
        'first_name':'Jonathan',
        'middle_name':'Middle',
        'last_name':'Frafer',
        'phone':'+44 161 4521 254',
        'register_address':'60 Westfield Road, Barton-Upon-Humber, DN18',
        'history_property_address':'34 Abbots Road, Abbots Langley, WD5',
        'property_address':'2 Fiars Terrace, Stafford, ST17',
        'year_built':'1900',
        'purchase_price':'110000',
        'monthly_rent':'1100',
        'property_type':'House - Mid terrace',
        'bedrooms':'2',
        'is_ex_local':'NO',
        'is_HMO':'NO',
        'loan_type':'new',
        'loan_years':'25',
        'loan_amount':'80000',
        'source_of_deposit':'Savings',
        'email': f'vasily.medved+{randint(11111,99999)}@djangostars.com',
        'password': 'qqweqqwe',
        'birth_date': APPLICANT_DOB
    }
    return applicant

def molo_address(browser, element, value):
    element.send_keys(value)
    sleep(1) #TBD refactor to avoid dumb wait
    browser.switch_to.active_element.send_keys(Keys.DOWN)
    browser.switch_to.active_element.send_keys(Keys.ENTER)

#@pytest.mark.skip
def test_create_new_user(browser,applicant):
    # 1. Open {server} and go to default calculator page
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

    # go to User data page
    page.submit_button.click()
    page = DipUDataPage(browser)
    assert page.tell_us.text == 'TELL US A BIT ABOUT YOURSELF'
    page.mr_choise.click()
    if applicant['title'] == 'mr':
        page.mr_choise_mr.click()
        sleep(1)
    page.first_name_input.send_keys(applicant['first_name'])
    page.first_name_input.click()
    page.last_name_input.send_keys(applicant['last_name'])
    page.phone_input.send_keys(applicant['phone'])
    page.birth_date_input.send_keys(applicant['birth_date'])
    page.address_input.click()
    molo_address(browser, page.address_input, applicant['register_address'])
    #
    page.email_input.send_keys(applicant['email'])
    page.password_input.send_keys(applicant['password'])

    # go to Consent page
    page.submit_button.click()
    page = DipConsentPage(browser)
    browser.find_element_by_xpath('//input[@data-test="consents-dip_common"]').click()
    browser.find_element_by_xpath('//input[@data-test="consents-marketing"]').click()
    page.soft_credit_check_checkbox.click()
    page.privacy_policy_checkbox.click()
    page.submit_button.click()
    browser.implicitly_wait(10)
    assert browser.current_url == "https://dev.app.molofinance.com/almost"
    assert browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/h2').text == 'ON YOUR WAY TO AN INSTANT MORTGAGE!'
    print(applicant['email'])
    #browser.close()

#@pytest.mark.skip
def test_login_and_be_happy_registered_user(browser,applicant):
    page = LoginPage(browser, 'https://molo:lambda@dev.app.molofinance.com/login/')
    # Must reopen the page again since Selenium have no normal ability to do basic auth, and MOLO brakes when opened with creds in URL
    # see 'https://github.com/w3c/webdriver/issues/385'
    browser.get('https://dev.app.molofinance.com/login/')
    page.email_input.send_keys('vasily.medved+94364@djangostars.com')
    page.password_input.send_keys(applicant['password'])
    page.login_button.click()
    sleep(5)

    #
    page = DashboardPage(browser, 'https://dev.app.molofinance.com/dashboard')
    # Check if button Start DIP shown (means that user is new and fresh). If not we proceed straight to property history page OR to property page in case when history property is already entered
    if page.action_button.text == 'START DIP':
        # Congrats page
        page.action_button.click()
        sleep(5)
        page = CongratsPage(browser)
        sleep(5)
        page.submit_button.click()
    elif page.action_button.text == 'PROPERTY EVALUATION':
        # Property history page
        page.action_button.click()
        page = PropertyPage(browser)
        molo_address(browser, page.history_property, applicant['history_property_address'])
        sleep(5)
    page.action_button.click()

    # Property details page
    page = PropertyPage(browser)
    molo_address(browser, page.address_input, applicant['property_address'])
    page.built_year_input.send_keys(applicant['year_built'])
    page.property_price_input.send_keys(applicant['purchase_price'])
    page.monthly_rent_input.send_keys(applicant['monthly_rent'])
    page.bedroooms_qty_input.send_keys(applicant['bedrooms'])
    page.property_type_dropdown.click()
    sleep(1)
    if applicant['property_type'] == 'House - Mid terrace':
        page.property_type_mid_terrace_choice.click()
    sleep(1000)

    '''
    page.history_property.send_keys(applicant['history_property_address'])
    sleep(1)  # TBD refactor to avoid dumb wait
    browser.switch_to.active_element.send_keys(Keys.DOWN)
    browser.switch_to.active_element.send_keys(Keys.ENTER)
    '''