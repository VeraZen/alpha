class ProductSelectorPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.get(url)

    @property
    def driver(self):
        return self.browser.driver

    @property
    def loan_type_button(self):
        return self.browser.find_element_by_xpath('//span[text()="Purchase"]')

    @property
    def user_loan_amount_input(self):
        return self.browser.find_element_by_name('desired_loan_amount')

    @property
    def deposit_selector(self):
        return self.browser.find_element_by_xpath('//div[@data-test="dip-application-loan-deposit-select"]')

    @property
    def loan_term_input(self):
        return self.browser.find_element_by_xpath('//div[@data-test="dip-application-loan-term-input"]')

    @property
    def product_list_table(self):
        return  self.browser.find_element_by_xpath('//div[@data-test="dip-products-list-option"]')

    @property
    def product_checkbox(self):
        return self.browser.find_elements_by_xpath('//input[@name="product_id"]')[0]

    @property
    def choose_product_button(self):
        return self.browser.find_element_by_xpath('//div[@data-test="dip-application-product-modal-continue-submit"]')

    @property
    def submit_button(self):
        return self.browser.find_element_by_xpath('//button[@data-test="dip-application-product-continue-submit"]')

    @property
    def x_button(self):
        return self.browser.find_element_by_xpath('//div[text()="✕"]')    \


    @property
    def confirm_selection_button(self):
        return self.browser.find_element_by_xpath('//button')
