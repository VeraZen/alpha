class LeadDetails:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    @property
    def notification_alert(self):
        return self.browser.find_by_xpath('//*[@class="notification-title"]')

    # Leads contact details

    @property
    def salutation_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/p[1]')  # noqa

    @property
    def first_name_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/p[2]')  # noqa

    @property
    def last_name_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/p[3]')  # noqa

    @property
    def birthdate_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/p[4]')  # noqa

    @property
    def department_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/p[5]')  # noqa

    @property
    def email_primary_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/p[6]')  # noqa

    @property
    def emails_other_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/p[7]')  # noqa

    @property
    def mobile_phone_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/p[1]')  # noqa

    @property
    def mobile_phone_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/p[1]')  # noqa

    @property
    def office_phone_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/p[2]')  # noqa

    @property
    def home_phone_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/p[3]')  # noqa

    @property
    def other_phone_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/p[4]')  # noqa

    @property
    def fax_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/p[5]')  # noqa

    @property
    def do_not_call_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/p[6]')  # noqa

    @property
    def facebook_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/p[7]')  # noqa

    @property
    def twitter_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/p[8]')  # noqa

    @property
    def googleplus_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/div[2]/p[9]')  # noqa

    # Address details

    @property
    def street_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/p[1]')  # noqa

    @property
    def city_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/p[2]')  # noqa

    @property
    def state_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/p[3]')  # noqa

    @property
    def postal_code_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/p[1]')  # noqa

    @property
    def country_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/p[2]')  # noqa

    # Lead source info

    @property
    def assigned_to_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/p[1]')  # noqa

    @property
    def lead_source_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/p[2]')  # noqa

    @property
    def lead_source_descr_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/p[3]')  # noqa

    @property
    def reffered_by_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/p[1]')  # noqa

    @property
    def status_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/p[2]')  # noqa

    @property
    def status_descr_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/p[3]')  # noqa

    # Assistant

    @property
    def assistant_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/p')  # noqa

    @property
    def assistant_phone_details(self):
        return self.browser.find_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/p')  # noqa

    # Activity

    @property
    def activity_notes_tab(self):
        return self.browser.find_by_id('activity-tabs-tab-notes')

    @property
    def activity_note_content(self):
        return self.browser.find_by_xpath('//*[@id="activity-tabs-pane-notes"]/div/div/div')
