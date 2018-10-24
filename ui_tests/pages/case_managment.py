class CaseManagment:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    @property
    def tenant_logo(self):
        return self.browser.is_element_visible_by_xpath('/html/body/div/div[1]/nav/div/div/a/div', wait_time=5)

    @property
    def title(self):
        return self.browser.title

    @property
    def layout_title(self):
        return self.browser.find_by_xpath('/html/body/div/div[1]/div/div[1]/div/h1').first

    @property
    def url(self):
        return self.browser.url
