import pytest

from solastis.ui_tests.tests.conftest import TEST_TENANT_URL, TEST_USER_PASSWORD

from solastis.ui_tests.pages.signin import SignIn
from solastis.ui_tests.pages.case_managment import CaseManagment


@pytest.mark.smoke
def test_signin(browser, live_server, tenant_admin, tenant):
    # Login
    page = SignIn(browser, TEST_TENANT_URL)
    page.email_field.fill(tenant_admin.email)
    page.password_field.fill(TEST_USER_PASSWORD)
    page.sign_in_button.click()
    page = CaseManagment(browser)
    assert page.tenant_logo
    assert page.url == TEST_TENANT_URL + 'case-management'
