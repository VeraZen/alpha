class AddressPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    @property
    def driver(self):
        return self.browser.driver

    @property
    def email_input(self):
        return self.browser.find_by_name('company_number')

    @property
    def submit_button(self):
        return self.browser.find_by_xpath('//button[@type="button"]')
