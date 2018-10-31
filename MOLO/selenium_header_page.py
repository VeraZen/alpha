class HeaderPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    @property
    def driver(self):
        return self.browser.driver

    @property
    def molo_logo(self):
        return self.browser.find_by_xpath('//span[@class="logo-molo"]')

    @property
    def your_account_menu(self):
        return self.browser.find_by_xpath('//span[@class="_1OtP83z-IB"]')

    @property
    def dashboard_menu(self):
        return self.browser.find_by_xpath('//a[@href="/dashboard"]')

    @property
    def profile_menu(self):
        return self.browser.find_by_xpath('//a[@href="/profile"]')

    @property
    def calculator_menu(self):
        return self.browser.find_by_xpath('//a[@href="/calculator"]')

    @property
    def logout_menu(self):
        return self.browser.find_by_xpath('//*[@id="root"]/header/div/div/div/ul/li[4]/a')
