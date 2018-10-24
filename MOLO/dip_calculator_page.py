class DipCalcPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    @property
    def driver(self):
        return self.browser.driver

    @property
    def company_button(self):
        return self.browser.find_by_xpath('/html/body/div[3]/div/div[1]/form/div[1]/div/div/div/label[2]')

    @property
    def remort_borrow_more_button(self):
        return self.browser.find_by_xpath('//*[@data-test="dip-radio-item-mortgage-type-remortgage-current"]')

    @property
    def income_input(self):
        return self.browser.find_by_xpath('//input[@data-test="dip-customer-income-input"]')

    @property
    def rent_input(self):
        return self.browser.find_by_xpath('//input[@data-test="dip-rent-amount"]')

    @property
    def property_value_input(self):
        return self.browser.find_by_xpath('//input[@name="property_value"]')

    @property
    def desired_loan_amount_input(self):
        return self.browser.find_by_xpath('//input[@name="desired_loan_amount"]')

    @property
    def submit_button(self):
        return self.browser.find_by_xpath('//button[@type="submit"]')
