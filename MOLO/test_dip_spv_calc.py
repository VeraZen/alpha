import pytest
from splinter import Browser
from selenium.webdriver.common.keys import Keys
from time import sleep
from dip_calculator_page import DipCalcPage
from dip_user_data_page import DipUDataPage
from dip_consent_page import DipConsentPage
from dip_almost_page import DipAlmostPage

@pytest.fixture
def browser():
    instance = Browser('firefox', headless=False)
    instance.driver.maximize_window()
    instance.driver.implicitly_wait(10)
    return instance


def test_dip_spv_calc(browser):
    # Test verifies the
    page = DipCalcPage(browser, 'https://dev.app.molofinance.com/calculator/')
    browser.visit("https://dev.app.molofinance.com/calculator/")
    page.company_button.click()

    #check the default data in fields
    assert page.income_input['value'] == '60,000'
    assert page.rent_input['value'] == '1,100'
    assert page.property_value_input['value'] == '250,000'
    assert page.desired_loan_amount_input['value'] == '200,000'

    page.income_input.click()
    page.driver.switch_to_active_element().send_keys(Keys.CONTROL + "a")
    page.driver.switch_to_active_element().send_keys(Keys.DELETE)
    page.income_input.fill('40000')
    sleep(3)
    page.property_value_input.click()
    page.driver.switch_to_active_element().send_keys(Keys.CONTROL + "a")
    page.driver.switch_to_active_element().send_keys(Keys.DELETE)
    page.property_value_input.fill('800000')
    sleep(3)
    assert page.desired_loan_amount_input['value'] == '302,578'
    page.submit_button.click()
    #Enter valid User data
    page = DipUDataPage(browser)
    page.salut_dropdown.click()
    page.mr_choise.click()
    sleep(2)
    page.first_name_input.fill('Daenerys')
    page.middle_name_input.fill('Blondie')
    page.last_name_input.fill('Targaryen')
    page.birth_date_input.fill('11111979')
    page.phone_input.fill('441617777777')
    page.address_input.fill('zebra')
    assert page.address_list
    page.driver.switch_to_active_element().send_keys(Keys.DOWN)
    page.driver.switch_to_active_element().send_keys(Keys.ENTER)
    page.email_input.fill('test@mail.ua')
    page.password_input.fill('Tigran2010')
    page.marketing_consent.check()
    page.submit_button.click()
    #Fill Conserns
    page = DipConsentPage(browser)
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
    assert browser.find_by_xpath('//*[@data-test="dip-email-verified-continue-submit"]').visible is True

