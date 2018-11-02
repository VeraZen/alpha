class HeaderPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.get(url)

    @property
    def driver(self):
        return self.browser.driver

    @property
    def molo_logo(self):
        return self.browser.find_element_by_xpath('//span[@class="logo-molo"]')

    @property
    def your_account_menu(self):
        return self.browser.find_element_by_xpath('//*[@id="root"]/header/div/div/div/span')

    @property
    def dashboard_menu(self):
        return self.browser.find_element_by_xpath('//a[@href="/dashboard"]')

    @property
    def profile_menu(self):
        return self.browser.find_element_by_xpath('//a[@href="/profile"]')

    @property
    def calculator_menu(self):
        return self.browser.find_element_by_xpath('//a[@href="/calculator"]')

    @property
    def logout_menu(self):
        return self.browser.find_element_by_xpath('//*[@id="root"]/header/div/div/div/ul/li[4]/a')
