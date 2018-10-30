class CongratsPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.get(url)

    @property
    def driver(self):
        return self.browser.driver

    @property
    def submit_button(self):
        return self.browser.find_element_by_xpath('//button[@data-test="dip-start-application-submit"]')

    @property
    def update_details_link(self):
        return self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/a')

    @property
    def download_dip_pdf_link(self):
        return self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/button[2]')

    @property
    def email_dip_pdf_link(self):
        return self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/button[3]')
