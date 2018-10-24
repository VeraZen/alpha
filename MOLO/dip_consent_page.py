class DipConsentPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    @property
    def driver(self):
        return self.browser.driver

    @property
    def required_warning(self):
        return self.browser.find_by_xpath('//*[@class="jss315 _24gjtBtiW- jss316"]')

    @property
    def uk_resident_checkbox(self):
        return self.browser.find_by_xpath('//input[@data-test="consents-uk_resident"]')

    @property
    def no_bankrupt_checkbox(self):
        return self.browser.find_by_xpath('//input[@data-test="consents-not_bankrupt"]')

    @property
    def property_england_checkbox(self):
        return self.browser.find_by_xpath('//input[@data-test="consents-property_in_england_or_wales"]')

    @property
    def personal_guarantee_checkbox(self):
        return self.browser.find_by_xpath('//input[@data-test="consents-ltd_company_personal_guarantee"]')

    @property
    def investment_purposes_checkbox(self):
        return self.browser.find_by_xpath('//input[@data-test="consents-renting_for_investment_purposes"]')

    @property
    def other_mortgages_checkbox(self):
        return self.browser.find_by_xpath('//input[@data-test="consents-mortgages_on_other_btl_properties"]')

    @property
    def no_consumer_btl_checkbox(self):
        return self.browser.find_by_xpath('//input[@data-test="consents-molo_not_offer_consumer_btl"]')

    @property
    def no_hmo_properties_checkbox(self):
        return self.browser.find_by_xpath('//input[@data-test="consents-molo_not_offer_hmo_properties"]')

    @property
    def single_applicant_checkbox(self):
        return self.browser.find_by_xpath('//input[@data-test="consents-apply_as_single_applicant_only"]')

    @property
    def soft_credit_check_checkbox(self):
        return self.browser.find_by_xpath('//input[@data-test="consents-allow_soft_credit_search"]')

    @property
    def privacy_policy_checkbox(self):
        return self.browser.find_by_xpath('//input[@data-test="consents-accept_privacy_policy"]')

    @property
    def submit_button(self):
        return self.browser.find_by_xpath('//button[@type="submit"]')
