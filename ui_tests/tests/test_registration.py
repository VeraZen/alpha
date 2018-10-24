import pytest

from solastis.ui_tests.tests.conftest import TEST_TENANT_URL, SOLASTIS_LOCAL_URL, TEST_TENANT_SUBDOMAIN

from solastis.ui_tests.pages.signup import SignUp
from solastis.ui_tests.pages.case_managment import CaseManagment


def test_signup(browser, live_server):

    page = SignUp(browser, SOLASTIS_LOCAL_URL)
    page.welcome_button.click()
    page.tenant_name_field.fill('SomeName')
    page.subdomain_field.fill(TEST_TENANT_SUBDOMAIN)
    page.email_field.fill('some@example.com')
    page.name_field.fill('Test')
    page.surname_field.fill('Testovisch')
    page.phone_field.fill('+380959302858')
    page.signup_button.click()

    page = CaseManagment(browser)
    assert page.title == 'Solastis CRM'
    assert page.layout_title
    assert page.layout_title.text == 'MANAGE CASES'
    assert page.tenant_logo
    assert page.url == TEST_TENANT_URL + 'case-management/#'
