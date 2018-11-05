class ProductTerms:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.get(url)


    @property
    def driver(self):
        return self.browser.driver

    @property
    def automated_assessment_checkbox(self):
        return self.browser.find_element_by_xpath('//input[@data-test="consents-molo_automated_assessment"]')    \

    @property
    def full_credit_search_checkbox(self):
        return self.browser.find_element_by_xpath('//input[@data-test="consents-allow_full_credit_search"]')

    @property
    def allow_fraud_checkbox(self):
        return self.browser.find_element_by_xpath('//input[@data-test="consents-allow_fraud_check"]')

    @property
    def mortgage_conditions_checkbox(self):
        return self.browser.find_element_by_xpath('//input[@data-test="consents-accept_molo_mortgage_conditions"]')    \

    @property
    def submit_button(self):
        return self.browser.find_element_by_xpath('//button[@data-test="dip-application-terms-conditions-continue-submit"]')
