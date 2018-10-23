class LeadCreateForm:
    def __init__(self, browser, url=None):
        self.browser = browser
        if url:
            self.browser.visit(url)

    @property
    def notification_alert(self):
        return self.browser.find_by_xpath('//*[@class="notification-title"]')

    # Contact details

    @property
    def driver(self):
        return self.browser.driver

    @property
    def salutation_dropdown(self):
        return self.browser.find_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div/span[1]/div[1]')  # noqa

    @property
    def salutation_choice_mr(self):
        return self.browser.find_by_text('Mr')

    @property
    def first_name_field(self):
        return self.browser.find_by_name('firstName')

    @property
    def last_name_field(self):
        return self.browser.find_by_name('lastName')

    @property
    def birthday_field(self):
        return self.browser.find_by_xpath('//*[@placeholder="Enter birthdate"]')

    @property
    def birthday_day(self):
        return self.browser.find_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[4]/div/div/div/table/tbody/tr[1]/td[1]')  # noqa

    @property
    def department_field(self):
        return self.browser.find_by_name('department')

    @property
    def emails_field(self):
        return self.browser.find_by_name('emails')

    @property
    def mobile_phone_field(self):
        return self.browser.find_by_xpath('//*[@type="tel"]')[0]

    @property
    def office_phone_field(self):
        return self.browser.find_by_xpath('//*[@type="tel"]')[1]

    @property
    def home_phone_field(self):
        return self.browser.find_by_xpath('//*[@type="tel"]')[2]

    @property
    def other_phone_field(self):
        return self.browser.find_by_xpath('//*[@type="tel"]')[3]

    @property
    def fax_field(self):
        return self.browser.find_by_xpath('//*[@type="tel"]')[4]

    @property
    def do_not_call_checkbox(self):
        return self.browser.find_by_xpath('//label[@class="form-checkbox-wrapper "]')

    @property
    def facebook_field(self):
        return self.browser.find_by_name('facebook')

    @property
    def twitter_field(self):
        return self.browser.find_by_name('twitter')

    @property
    def googleplus_field(self):
        return self.browser.find_by_name('googleplus')

    # Lead address

    @property
    def primary_address_street_field(self):
        return self.browser.find_by_name('primaryAddressStreet')

    @property
    def primary_address_city_field(self):
        return self.browser.find_by_name('primaryAddressCity')

    @property
    def primary_address_state_field(self):
        return self.browser.find_by_name('primaryAddressState')

    @property
    def primary_address_postal_code_field(self):
        return self.browser.find_by_name('primaryAddressPostalcode')

    @property
    def primary_address_country_dropdown(self):
        return self.browser.find_by_text('Select country')

    @property
    def primary_address_country_choice_albania(self):
        return self.browser.find_by_text('Albania')

    # Lead source info

    @property
    def agent_dropdown(self):
        return self.browser.find_by_text('Select agent')

    @property
    def agent_choice_user(self):
        return self.browser.find_by_text('Voldemar Pupkin')

    @property
    def lead_source_dropdown(self):
        return self.browser.find_by_text('Simple text')

    @property
    def source_choice_web(self):
        return self.browser.find_by_text('Web')

    @property
    def lead_source_description_field(self):
        return self.browser.find_by_name('leadSourceDescription')

    @property
    def referred_by_field(self):
        return self.browser.find_by_name('referredBy')

    @property
    def status_dropdown(self):
        return self.browser.find_by_text('Select status')

    @property
    def status_choice_new(self):
        return self.browser.find_by_text('New')

    @property
    def status_description_field(self):
        return self.browser.find_by_name('statusDescription')

    # Assistant

    @property
    def assistant_field(self):
        return self.browser.find_by_name('assistant')

    @property
    def assistantPhone_field(self):
        return self.browser.find_by_name('assistantPhone')

    # Notes

    @property
    def note_title_input(self):
        return self.browser.find_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div[6]/div[2]/div/div/div/div/div[1]/input')  # noqa

    @property
    def note_text_input(self):
        return self.browser.find_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div[6]/div[2]/div/div/div/div/div[2]/textarea')  # noqa

    @property
    def create_lead_button(self):
        return self.browser.find_by_xpath('/html/body/div[2]/div[2]/div/div/form/div[3]/button[2]')
