class PropertyPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.get(url)

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
        return self.browser.find_element_by_xpath('//div[@data-test="dip-application-property-type-select"]')

    @property
    def property_type_mid_terrace_choice(self):
        return self.browser.find_element_by_xpath('//li[@data-test="dip-select-menu-item-property-type-house-mid-terrace"]')

    @property
    def property_construction_material_dropdown(self):
        return self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/form/div[7]/div/div/div[2]')

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
    def continue_button(self):
        return self.browser.find_element_by_xpath('//input[@data-test="dip-application-property-continue-submit"]')
