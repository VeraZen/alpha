class PropertyPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    @property
    def driver(self):
        return self.browser.driver

    @property
    def address_input(self):
        return self.browser.find_by_xpath('//input[@data-test="dip-application-property-address-search"]')

    @property
    def built_year_input(self):
        return self.browser.find_by_xpath('//input[@data-test="dip-application-property-year-built-input"]')

    @property
    def monthly_rent_input(self):
        return self.browser.find_by_name('monthly_rent')

    @property
    def bedroooms_qty_input(self):
        return self.browser.find_by_name('property_bedrooms')

    @property
    def property_type_dropdown(self):
        return self.browser.find_by_xpath('//input[@data-test="dip-application-property-type-select"]')

    @property
    def exlocal_yes_radiobutton(self):
        return self.browser.find_by_xpath('//input[@name="is_property_ex_local"][@value="true"]')

    @property
    def exlocal_no_radiobutton(self):
        return self.browser.find_by_xpath('//input[@name="is_property_ex_local"][@value="false"]')

    @property
    def hmo_yes_radiobutton(self):
        return self.browser.find_by_xpath('//input[@name="is_property_hmo"][@value="true"]')

    @property
    def continue_button(self):
        return self.browser.find_by_xpath('//input[@data-test="dip-application-property-continue-submit"]')
