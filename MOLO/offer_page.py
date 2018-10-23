class OfferPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    @property
    def driver(self):
        return self.browser.driver

    @property
    def loan_sum_text(self):
        return self.browser.find_by_xpath('//p[@class="primary-text"]')

    @property
    def email_offer_pdf_link(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div/div[1]/div/button[1]')

    @property
    def download_offer_pdf_link(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div/div[1]/div/button[2]')

    @property
    def download_terms_link(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div/div[1]/div/a[1]')

    @property
    def download_tariffs_link(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div/div[1]/div/a[2]')

    @property
    def dashboard_button(self):
        return self.browser.find_by_xpath('//a[@role="button"][@href="/dashboard"]')
