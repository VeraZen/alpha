from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class PropertyPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.get(url)

    def fluent_wait(self, selector, method, action, to_sleep=0, polling_rate=1, timeout=10):
        sleep(to_sleep)
        wait_obj = WebDriverWait(
           self.browser, timeout, polling_rate,
           ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException]
        )
        return wait_obj.until(action((method, selector)))

    @property
    def driver(self):
        return self.browser.driver

    @property
    def history_property(self):
        return self.browser.find_element_by_xpath('//input[@data-test="dip-application-history-address-search"]')

    @property
    def history_page_submit_button(self):
        return self.browser.find_element_by_xpath('//button[@data-test="dip-application-address-verification-continue-submit"]')

    @property
    def property_price_input(self):
        return self.browser.find_element_by_xpath('//input[@data-test="dip-application-property-price-input"]')

    @property
    def address_input(self):
        return self.browser.find_element_by_xpath('//input[@data-test="dip-application-property-address-search"]')

    @property
    def built_year_input(self):
        return self.browser.find_element_by_xpath('//input[@data-test="dip-application-property-year-built-input"]')

    @property
    def monthly_rent_input(self):
        return self.browser.find_element_by_name('monthly_rent')

    @property
    def bedroooms_qty_input(self):
        return self.browser.find_element_by_name('property_bedrooms')

    @property
    def property_type_dropdown(self):
        return self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/form/div[6]/div/div/div[2]/div/div')

    @property
    def property_type_mid_terrace_choice(self):
        return self.browser.find_element_by_xpath('//li[@data-test="dip-select-menu-item-property-type-house-mid-terrace"]')
        # return self.browser.find_element_by_xpath('//*[@id="menu-type"]/div[2]/ul/li[4]')

    @property
    def property_construction_material_dropdown(self):
        return self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/form/div[7]/div/div/div[2]')

    @property
    def property_construction_material_choise(self):
        return self.browser.find_element_by_xpath('//li[@data-value="standard"]')

    @property
    def exlocal_yes_radiobutton(self):
        return self.browser.find_element_by_xpath('//input[@name="is_property_ex_local"][@value="true"]')

    @property
    def exlocal_no_radiobutton(self):
        return self.browser.find_element_by_xpath('//input[@name="is_property_ex_local"][@value="false"]')

    @property
    def hmo_yes_radiobutton(self):
        return self.browser.find_element_by_xpath('//input[@name="is_property_hmo"][@value="true"]')

    @property
    def hmo_no_radiobutton(self):
        return self.browser.find_element_by_xpath('//input[@name="is_property_hmo"][@value="false"]')

    @property
    def continue_button(self):
        return self.browser.find_element_by_xpath('//button[@data-test="dip-application-property-continue-submit"]')
