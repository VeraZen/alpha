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


