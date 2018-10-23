class LeadsPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    # Leads page elements
    @property
    def tenant_logo(self):
        return self.browser.is_element_visible_by_xpath('/html/body/div/div[1]/nav/div/div/a/div', wait_time=5)

    @property
    def driver(self):
        return self.browser.driver

    @property
    def leads_header_button(self):
        return self.browser.find_by_xpath("//*[@id='nav-drop-down']").first

    @property
    def create_lead_header_menu(self):
        return self.browser.find_by_xpath('/html/body/div/div[1]/nav/div/ul[1]/li[1]/ul/li[1]/a')

    # Leads table

    @property
    def last_name_table(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]/a')  # noqa

    @property
    def email_table(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[6]')  # noqa

    @property
    def edit_action(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[10]/div/button[2]')  # noqa

    @property
    def notification_alert(self):
        return self.browser.find_by_xpath('//*[@class="notification-title"]')
