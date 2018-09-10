class DipUDataPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    @property
    def driver(self):
        return self.browser.driver

    @property
    def salut_dropdown(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div/div[1]/div/form/div[1]/div[1]/div/div/div/div')

    @property
    def mr_choise(self):
        return self.browser.find_by_xpath('//*[@id="menu-customers[0].title"]/div[2]/ul/li[1]')

    @property
    def first_name_input(self):
        return self.browser.find_by_xpath('//input[@name="customers[0].first_name"]')

    @property
    def last_name_input(self):
        return self.browser.find_by_xpath('//input[@name="customers[0].last_name"]')

    @property
    def birth_date_input(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div/div[1]/div/form/div[2]/div[1]/div/div/input')

    @property
    def phone_input(self):
        return self.browser.find_by_xpath('//input[@name="customers[0].mobile"]')

    @property
    def address_input(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div/div[1]/div/form/div[3]/div/div/div/div/div[1]/div/input')

    @property
    def address_list(self):
        return self.browser.is_element_visible_by_xpath('//div[@role="menuitem"]', wait_time=5)

    @property
    def email_input(self):
        return self.browser.find_by_xpath('//input[@name="customers[0].email"]')

    @property
    def password_input(self):
        return self.browser.find_by_xpath('//input[@name="customers[0].password"]')

    @property
    def marketing_consent(self):
        return self.browser.find_by_xpath('//input[@type="checkbox"]')

    @property
    def submit_button(self):
        return self.browser.find_by_xpath('//button[@type="submit"]')
