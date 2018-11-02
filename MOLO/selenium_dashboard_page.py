class DashboardPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.get(url)

    @property
    def driver(self):
        return self.browser.driver

    @property
    def first_status(self):
        return self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/div[1]/header/span[1]')

    @property
    def my_mortages_table(self):
        return self.browser.find_element_by_xpath('//div[@data-test="dip-dashboard-mortgages-list-table"]')

    @property
    def second_status(self):
        return self.browser.find_element_by_xpath('//span[@data-test="dip-dashboard-mortgage-status"]')

    @property
    def main_applicant(self):
        return self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/div[1]/div/div/div[1]/p[2]')

    @property
    def property_address(self):
        return self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/div[1]/div/div/div[3]/p[2]')

    @property
    def action_button(self):
        return self.browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/div/div/div/div[4]/a')
