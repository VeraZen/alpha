class LoginPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    @property
    def driver(self):
        return self.browser.driver

    @property
    def email_input(self):
        return self.browser.find_by_name('email')

    @property
    def password_input(self):
        return self.browser.find_by_name('password')

    @property
    def remember_checkbox(self):
        return self.browser.find_by_xpath('//input[@type="checkbox"]')

    @property
    def login_button(self):
        return self.browser.find_by_xpath('//button[@type="submit"]')

    @property
    def forgot_password_link(self):
        return self.browser.find_by_xpath('//a[@href="/forgot"]')

    @property
    def signup_link(self):
        return self.browser.find_by_xpath('//a[@href="/calculator"]')

