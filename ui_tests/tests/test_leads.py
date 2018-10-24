import pytest

from time import sleep

from selenium.webdriver.common.keys import Keys
from solastis.ui_tests.tests.conftest import TEST_TENANT_URL, TEST_USER_PASSWORD

from solastis.ui_tests.pages.leads.leads_page import LeadsPage
from solastis.ui_tests.pages.leads.lead_create_form import LeadCreateForm
from solastis.ui_tests.pages.leads.lead_details import LeadDetails

from solastis.ui_tests.pages.signin import SignIn


def test_lead_creation_min_req(browser, live_server, tenant_admin, tenant):
    # Check Lead is saved with mandatory fields filled only
    # Login
    page = SignIn(browser, TEST_TENANT_URL)
    page.email_field.fill(tenant_admin.email)
    page.password_field.fill(TEST_USER_PASSWORD)
    page.sign_in_button.click()
    # test creating the Lead
    assert page.tenant_logo
    page = LeadsPage(browser, TEST_TENANT_URL+'leads')
    assert page.tenant_logo
    page.leads_header_button.click()
    page.create_lead_header_menu.click()
    page = LeadCreateForm(browser)
    page.last_name_field.fill('Mao')
    page.emails_field.fill('mao@mail.chi')
    page.create_lead_button.click()
    # check if the created lead is shown in leads table
    page = LeadsPage(browser)
    assert page.last_name_table.text == 'Mao'
    assert page.email_table.text == 'mao@mail.chi'
    assert page.notification_alert.text == 'Lead has been created successfully'

@pytest.mark.current
def test_lead_creation_all_fields(browser, live_server, tenant_admin):
    # Login
    page = SignIn(browser, TEST_TENANT_URL)
    page.email_field.fill(tenant_admin.email)
    page.password_field.fill(TEST_USER_PASSWORD)
    page.sign_in_button.click()
    # test creating the Lead
    assert page.tenant_logo
    page = LeadsPage(browser, TEST_TENANT_URL + 'leads/#')
    assert page.tenant_logo
    page.leads_header_button.click()
    page.create_lead_header_menu.click()
    # fill the form (lead contact details)
    page = LeadCreateForm(browser)
    page.salutation_dropdown.click()
    page.salutation_choice_mr.click()
    page.first_name_field.fill('FMao')
    page.last_name_field.fill('Mao')
    page.birthday_field.click()
    page.birthday_day.click()
    page.department_field.fill ('Sales and Mark')
    page.emails_field.fill('mao@mail.chi')
    page.mobile_phone_field.fill('380930000000')
    page.office_phone_field.fill('380931111111')
    page.home_phone_field.fill('380932222222')
    page.other_phone_field.fill('380933333333')
    page.fax_field.fill('380934444444')
    page.do_not_call_checkbox.click()
    page.facebook_field.fill('fb')
    page.twitter_field.fill('twitt')
    page.googleplus_field.fill('google+')
    # fill the form (address)
    page.primary_address_street_field.fill('primstreet')
    page.primary_address_city_field.fill('primcity')
    page.primary_address_state_field.fill('primstate')
    page.primary_address_postal_code_field.fill('1234')
    page.primary_address_country_dropdown.click()
    page.primary_address_country_choice_albania.click()
    # fill the form (lead source info)
    page.lead_source_dropdown.click()
    page.source_choice_web.click()
    page.lead_source_description_field.fill('Lead comes from the darkness')
    page.agent_dropdown.click()
    page.driver.switch_to_active_element().send_keys(Keys.ENTER)
    page.referred_by_field.fill('Lucifer')
    page.status_dropdown.click()
    page.status_choice_new.click()
    page.status_description_field.fill('Status is blue as sky')
    # fill the form (assistant)
    page.assistant_field.fill('Ass-is-ant')
    page.assistantPhone_field.fill('380937777777')
    # fill the form (notes)
    page.note_title_input.click()
    page.note_title_input.fill('Nota Bene')
    page.note_text_input.fill('We all leave in a yellow submarine')
    page.create_lead_button.click()
    # check if the created lead is shown in leads table
    page = LeadsPage(browser)
    assert page.last_name_table.text == 'Mao'
    assert page.email_table.text == 'mao@mail.chi'
    assert page.notification_alert.text == 'Lead has been created successfully'
    page.last_name_table.click()
    # check if all data is shown in Lead details
    page = LeadDetails(browser)
    page.activity_notes_tab.click()
    # lead details. LEAD CONTACT DETAILS
    assert page.salutation_details.text == 'Salutation: mr'
    assert page.first_name_details.text == 'First name: FMao'
    assert page.last_name_details.text == 'Last name: Mao'
    assert page.birthdate_details.text != 'Birthdate:'
    assert page.department_details.text == 'Department: Sales and Mark'
    assert page.email_primary_details.text == 'Email (Primary): \nmao@mail.chi'
    assert page.emails_other_details.text == 'Email: \n-'
    assert page.mobile_phone_details.text == 'Mobile phone: +380930000000'
    assert page.office_phone_details.text == 'Office phone: +380931111111'
    assert page.home_phone_details.text == 'Home phone: +380932222222'
    assert page.other_phone_details.text == 'Other phone: +380933333333'
    assert page.fax_details.text == 'Fax: +380934444444'
    assert page.do_not_call_details.visible
    assert page.facebook_details.text == 'Facebook: fb'
    assert page.twitter_details.text == 'Twitter: twitt'
    assert page.googleplus_details.text == 'Google Plus ID: google+'
    # lead details. Address
    assert page.street_details.text == 'Street: primstreet'
    assert page.city_details.text == 'City: primcity'
    assert page.state_details.text == 'State: primstate'
    assert page.postal_code_details.text == 'Postal Code: 1234'
    assert page.country_details.text == 'County: Albania'
    # lead details. LEAD SOURCE INFO
    assert page.assigned_to_details.text == 'Assigned To: Voldemar Pupkin'
    assert page.lead_source_details.text == 'Lead Source: web'
    assert page.lead_source_descr_details.text == 'Lead Source Description: \n Lead comes from the darkness'
    assert page.reffered_by_details.text == 'Referred By: Lucifer'
    assert page.status_details.text == 'Status: New'
    assert page.status_descr_details.text == 'Status Description: \n Status is blue as sky'
    # lead details. ASSISTANT
    assert page.assistant_details.text == 'Type Name: Ass-is-ant'
    assert page.assistant_phone_details.text == 'Phone: 380937777777'
    # lead details. Activity tab
    assert 'Nota Bene' in page.activity_note_content.text
    assert 'We all leave in a yellow submarine' in page.activity_note_content.text
