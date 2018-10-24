class SignIn:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    @property
    def tenant_logo(self):
        return self.browser.is_element_visible_by_xpath('/html/body/div/div[1]/nav/div/div/a/div', wait_time=5)

    @property
    def sign_in_button(self):
        return self.browser.find_by_xpath('/html/body/div/div/div/div[2]/form/div[2]/button')

    @property
    def email_field(self):
        return self.browser.find_by_name('email')

    @property
    def password_field(self):
        return self.browser.find_by_name('password')

    @property
    def url(self):
        return self.browser.url
