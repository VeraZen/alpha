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
        return self.browser.find_by_xpath('//input[@data-test="dip-application-history-address-search"]')

    @property
    def add_address_button(self):
        return self.browser.find_by_xpath('//button[@class="jss195 jss1266 _1GpvsiAfwy jss1268 jss1270 jss1271 jss1273 _6l_6AYOjhh"]')

    @property
    def clear_address_button(self):
        return self.browser.find_by_xpath('//button[@class="jss195 jss1266 _1GpvsiAfwy jss1275 jss1276 AP0TqBd9Tf jss1278 jss1279 wJpghFpP3O"]')

    @property
    def continue_button(self):
        return self.browser.find_by_xpath('//input[@data-test="dip-application-address-verification-continue-submit"]')
