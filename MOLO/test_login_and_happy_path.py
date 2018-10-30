import pytest
from splinter import Browser
from selenium.webdriver.common.keys import Keys
from time import sleep
from dip_calculator_page import DipCalcPage
from dip_user_data_page import DipUDataPage
from datetime import date, datetime, timedelta
import random

@pytest.fixture
#test
def browser():
    instance = Browser('chrome', headless=False)
    instance.driver.maximize_window()
    instance.driver.implicitly_wait(15)
    return instance


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
        'address':'60 Westfield Road',
        'email': f'vasily.medved{random.randint(11111,99999)}@djangostars.com',
        'password': 'qqweqqwe',
        'birth_date': APPLICANT_DOB
    }
    return applicant.get(key)


def test_create_new_user(browser):
    # 1. Open {server}
    page = DipCalcPage(browser, 'https://dev.app.molofinance.com/calculator/')
    browser.visit("https://dev.app.molofinance.com/calculator/")
    #check the default data in fields - not that necessary actually)
    page.individual_button.click()
    assert page.income_input['value'] == '60,000'
    assert page.rent_input['value'] == '1,100'
    assert page.property_value_input['value'] == '250,000'
    assert page.desired_loan_amount_input['value'] == '200,000'

    # 2. On calculator page choose individual option, submit
    assert page.submit_button.first.value == 'Get approved now'.upper()
    page.individual_button.click()
    page.submit_button.click()

    # 3. Fill User Details page with next valid data, Submit:
    page = DipUDataPage(browser)
    assert page.tell_us.first.text == 'TELL US A BIT ABOUT YOURSELF'

    #mr
    page.mr_choise.click()
    if applicant('title') =='mr':
        page.mr_choise_mr.click()
        sleep(2)
    page.first_name_input.fill(applicant('first_name'))
    page.first_name_input.click()
    page.last_name_input.fill(applicant('last_name'))
    page.phone_input.fill(applicant('phone'))
    bd = page.birth_date_input
    bd.fill(applicant('birth_date'))
    page.address_input.click()
    page.address_input.fill(applicant('address'))
    # page.driver.switch_to_active_element().send_keys(Keys.CONTROL + "a")
    browser.switch_to_active_element().send_keys(Keys.DOWN)
    browser.switch_to_active_element().send_keys(Keys.ENTER)
    sleep(3)
    assert browser.url == "https://dev.app.molofinance.com/almost"
    sleep(5)

    #Fill user details with valid data




    # browser.close()

