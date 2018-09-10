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
        return self.browser.find_by_xpath('//*[@id="root"]/div/div[1]/div/form/div[1]/div/div/div/label[2]/span[2]')

    @property
    def remort_borrow_more_button(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div/div[1]/div/form/div[2]/div[1]/div/div/label[3]/span[2]')

    @property
    def income_input(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div/div[1]/div/form/div[2]/div[2]/div/div/div/input')

    @property
    def rent_input(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div/div[1]/div/form/div[3]/div[1]/div/div/div/input')

    @property
    def property_value_input(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div/div[1]/div/form/div[3]/div[2]/div/div/div/input')

    @property
    def desired_loan_amount_input(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div/div[1]/div/form/div[4]/div[1]/div/div/div/input')

    @property
    def submit_button(self):
        return self.browser.find_by_xpath('//button[@type="submit"]')
