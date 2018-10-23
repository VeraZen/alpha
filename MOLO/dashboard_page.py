class DashboardPage:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    @property
    def driver(self):
        return self.browser.driver

    @property
    def first_status(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/div[1]/header/span[1]')

    @property
    def second_status(self):
        return self.browser.find_by_xpath('//span[@data-test="dip-dashboard-mortgage-status"]')

    @property
    def main_applicant(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/div[1]/div/div/div[1]/p[2]')

    @property
    def property_address(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/div[1]/div/div/div[3]/p[2]')

    @property
    def action_button(self):
        return self.browser.find_by_xpath('//a[@class="jss182 jss3515 _1GpvsiAfwy jss3524 jss3525 AP0TqBd9Tf jss3527 jss3528 _38TTZ_TXw6"]')
