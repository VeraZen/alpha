class AddressPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    @property
    def driver(self):
        return self.browser.driver

    @property
    def user_loan_amount_input(self):
        return self.browser.find_by_name('desired_loan_amount')

    @property
    def deposit_selector(self):
        return self.browser.find_by_xpath('//div[@data-test="dip-application-loan-deposit-select"]')

    @property
    def loan_term_input(self):
        return self.browser.find_by_xpath('//div[@data-test="dip-application-loan-term-input"]')

    @property
    def product_checkbox(self):
        return self.browser.find_by_name('product_id').first

    @property
    def choose_product_button(self):
        return self.browser.find_by_xpath('//div[@data-test="dip-application-product-modal-continue-submit"]')

    @property
    def submit_button(self):
        return self.browser.find_by_xpath('//div[@data-test="dip-application-product-continue-submit"]')
