import pytest
from splinter import Browser

SOLASTIS_LOCAL_URL = 'http://localhost:3000/'
TEST_TENANT_URL = 'http://test.localhost:3000/'
TEST_USER_EMAIL = 'selenium@example.com'
TEST_USER_PASSWORD = '1qaz2wsxQ'
TEST_USER_FIRST_NAME = 'Voldemar'
TEST_USER_LAST_NAME = 'Pupkin'
TEST_TENANT_SUBDOMAIN = 'test'

@pytest.fixture
def browser():
    instance = Browser('firefox', headless=False)
    instance.driver.maximize_window()
    instance.driver.implicitly_wait(10)
    return instance


@pytest.fixture
def tenant_admin(db, tenant):
    from solastis.fixtures import create_tenant_user
    return create_tenant_user(TEST_USER_EMAIL, first_name=TEST_USER_FIRST_NAME, last_name=TEST_USER_LAST_NAME,
                              password=TEST_USER_PASSWORD, tenant=tenant, is_staff=True)
