class DipAlmostPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    @property
    def driver(self):
        return self.browser.driver

    @property
    def continue_button(self):
        return self.browser.find_by_xpath('//*[@data-test="dip-email-verified-continue-submit"]')
    @property
    def continue_button_visible(self):
        return self.browser.find_by_xpath('//*[@data-test="dip-email-verified-continue-submit"]').visible

    @property
    def resend_email_link(self):
        return self.browser.find_by_xpath('//*[@class="jss195 jss370 _1GpvsiAfwy jss372 _3DA8x8fr2B jss374 jss375"]')
