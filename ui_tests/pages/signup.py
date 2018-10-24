class SignUp:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    @property
    def tenant_name_field(self):
        return self.browser.find_by_name('name')

    @property
    def phone_field(self):
        return self.browser.find_by_xpath('/html/body/div/div[1]/div/div[2]/form/div[1]/div[6]/div/input')

    @property
    def subdomain_field(self):
        return self.browser.find_by_name('subdomain')

    @property
    def name_field(self):
        return self.browser.find_by_name('owner.firstName')

    @property
    def surname_field(self):
        return self.browser.find_by_name('owner.lastName')

    @property
    def email_field(self):
        return self.browser.find_by_name('owner.email')

    @property
    def signup_button(self):
        return self.browser.find_by_xpath('/html/body/div/div[1]/div/div[2]/form/div[2]/button')

    @property
    def welcome_button(self):
        return self.browser.find_link_by_href('/auth/signup')
