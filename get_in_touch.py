import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from time import sleep

dir = os.path.dirname(__file__)
chrome_driver_path = dir + '\chromedriver.exe'

class Get_In_Touch_Tests(unittest.TestCase):

    email_xpath = "//label[@for='id_email']/span"
    name_xpath = "//label[@for='id_full_name']/span"
    send_button_xpath = "//button[@class='green hvr-underline-from-center'][@type='submit']"

    name_error_border_xpath = "//form[@id='feedback_form']/div/div/span[@class='input input--madoka error']/input[@name='full_name']"
    email_error_border_xpath = "//form[@id='feedback_form']/div/div/span[@class='input input--madoka error']/input[@name='email']"

    email_green_border_xpath = "//form[@id='feedback_form']/div/div/span[@class='input input--madoka input--filled']/input[@name='email']"
    name_green_border_xpath = "//form[@id='feedback_form']/div/div/span[@class='input input--madoka input--filled']/input[@name='full_name']"
    phone_green_border_xpath = "//form[@id='feedback_form']/div/div/span[@class='input input--madoka input--filled']/input[@name='phone']"
    description_green_border_xpath = "//form[@id='feedback_form']/div/div/span[@class='input input--madoka input--filled']/textarea[@name='project_description']"

    email_input_id = 'id_email'
    name_input_id = 'id_full_name'
    phone_input_id = 'id_phone'
    description_input_id = 'id_project_description'

    greeting_1_xpath = "//div[@id='feedback']/div/div/h3[@class='secondary-title']"
    greeting_2_xpath = "//div[@id='feedback']/div/div/p[@class='sub-title']"

    web_platform_xpath = "//input[@name='platform'][@value='Web']"
    ios_platform_xpath = "//input[@name='platform'][@value='iOS']"
    android_platform_xpath = "//input[@name='platform'][@value='Android']"
    custom_platform_xpath = "//input[@name='platform'][@value='Custom']"

    platform_parameters_xpath = "//p[@class='js-checkbox-params']/span"

    prototype_xpath = "//input[@name='delivery'][@value='Prototype']"
    mvp_xpath = "//input[@name='delivery'][@value='MVP']"
    complete_xpath = "//input[@name='delivery'][@value='Complete']"
    existing_xpath = "//input[@name='delivery'][@value='Existing']"

    delivery_parameters_xpath = "//p[@class='js-radio-params']/span"

    ten_xpath = "//input[@name='budget'][@value='$10K - $25K']"
    twentyfive_xpath = "//input[@name='budget'][@value='$25K - $50K']"
    fifty_xpath = "//input[@name='budget'][@value='$50K - $100K']"
    hundred_xpath = "//input[@name='budget'][@value='$100K - $200K+']"

    budget_range_xpath = "//p[@class='js-range-params']/span"

    @classmethod
    def setUp(cls):
        cls.browser = webdriver.Chrome(chrome_driver_path)
        cls.browser.implicitly_wait(30)
        cls.browser.maximize_window()
        #basic https authentication login-djangostars, pass-ds2015
        cls.browser.get('https://djangostars:ds2015@beta.ds.inprogress.rocks/get-in-touch/')

    def test_elements_presence(self):

        browser = self.browser
        my_target_is = browser.find_element_by_xpath("//div[@id='feedback']/h2")
        self.assertEqual(my_target_is.text, 'MY TARGET IS')

        contact = browser.find_element_by_xpath("//form[@id='feedback_form']/div[1]/p")
        self.assertEqual(contact.text, 'Contact:')

        phone = browser.find_element_by_xpath("//label[@for='id_phone']/span")
        self.assertEqual(phone.text, 'Phone')

        description = browser.find_element_by_xpath("//label[@for='id_project_description']/span")
        self.assertEqual(description.text, 'Description')

        platform = browser.find_element_by_xpath("//form[@id='feedback_form']/div/p[@class='js-checkbox-params']")
        self.assertEqual(platform.text, 'Platform:')

        delivery = browser.find_element_by_xpath("//form[@id='feedback_form']/div/p[@class='js-radio-params']")
        self.assertEqual(delivery.text, 'Delivery:')

        budget_range = browser.find_element_by_xpath("//form[@id='feedback_form']/div/p[@class='js-range-params']")
        self.assertEqual(budget_range.text, 'Budget range:')

        choose_file = browser.find_element_by_xpath("//div[@id='uploadFile']/div/div/span")
        self.assertEqual(choose_file.text, 'Choose file or drag here')

        size_limit = browser.find_element_by_xpath("//div[@id='uploadFile']/div/div/p")
        self.assertEqual(size_limit.text, 'Size limit: 10MB')

        choose_file_icon = browser.find_element_by_xpath("//div[@id='uploadFile']/div/img[@src='/static/images/cloud-computing.svg']")
        self.assertTrue(choose_file_icon.is_displayed())

    def test_empty_send(self):

        browser = self.browser

        name = browser.find_element_by_xpath(self.name_xpath)
        self.assertEqual(name.text, 'Name*')

        email = browser.find_element_by_xpath(self.email_xpath)
        self.assertEqual(email.text, 'Email*')

        send_button = browser.find_element_by_xpath(self.send_button_xpath)

        # send with empty name+email, check red underline
        send_button.click()
        name_error_border = browser.find_element_by_xpath(self.name_error_border_xpath)
        email_error_border = browser.find_element_by_xpath(self.email_error_border_xpath)

        self.assertTrue(name_error_border.is_displayed())
        self.assertTrue(email_error_border.is_displayed())

    def test_invalid_email(self):

        browser = self.browser

        email = browser.find_element_by_xpath(self.email_xpath)
        send_button = browser.find_element_by_xpath(self.send_button_xpath)
        #ActionChains(browser).move_to_element(email).click(email).perform()

        email.click()
        email_green_border = browser.find_element_by_xpath(self.email_green_border_xpath)
        self.assertTrue(email_green_border.is_displayed())
        browser.find_element_by_id(self.email_input_id).send_keys('123456')
        send_button.click()

        email_error_border = browser.find_element_by_xpath(self.email_error_border_xpath)
        self.assertTrue(email_error_border.is_displayed())

        browser.get('https://beta.ds.inprogress.rocks/get-in-touch/')

        browser.find_element_by_xpath(self.email_xpath).click()
        browser.find_element_by_id(self.email_input_id).send_keys('вера@gmail.com')
        browser.find_element_by_xpath(self.send_button_xpath).click()

        email_error_border = browser.find_element_by_xpath(self.email_error_border_xpath)
        self.assertTrue(email_error_border.is_displayed())

    def test_valid_input(self):
        #check green borders around input fields + link to page + greeting message

        browser = self.browser
        name_input = browser.find_element_by_id(self.name_input_id)
        email_input = browser.find_element_by_id(self.email_input_id)
        phone_input = browser.find_element_by_id(self.phone_input_id)
        description_input = browser.find_element_by_id(self.description_input_id)

        send_button = browser.find_element_by_xpath(self.send_button_xpath)

        name_input.send_keys('123456')
        name_green_border = browser.find_element_by_xpath(self.name_green_border_xpath)
        self.assertTrue(name_green_border.is_displayed())

        email_input.send_keys('1@mail.ua')

        phone_input.send_keys('123')
        phone_green_border = browser.find_element_by_xpath(self.phone_green_border_xpath)
        self.assertTrue(phone_green_border.is_displayed())

        description_input.send_keys('123')
        description_green_border = browser.find_element_by_xpath(self.description_green_border_xpath)
        self.assertTrue(description_green_border.is_displayed())

        send_button.click()

        self.assertEqual(browser.current_url, 'https://djangostars:ds2015@beta.ds.inprogress.rocks/get-in-touch/#feedback')

        greeting_1 = browser.find_element_by_xpath(self.greeting_1_xpath)
        greeting_2 = browser.find_element_by_xpath(self.greeting_2_xpath)

        self.assertEqual(greeting_1.text, 'THANK YOU FOR YOUR FEEDBACK')
        self.assertEqual(greeting_2.text, "We'll reply you as soon as possible ;)")

    def test_platform_parameters(self):
        #check text near Platform when choosing the checkboxes

        browser = self.browser
        web_platform = browser.find_element_by_xpath(self.web_platform_xpath)
        ios_platform = browser.find_element_by_xpath(self.ios_platform_xpath)
        android_platform = browser.find_element_by_xpath(self.android_platform_xpath)
        custom_platform = browser.find_element_by_xpath(self.custom_platform_xpath)

        platform_parameters = browser.find_element_by_xpath(self.platform_parameters_xpath)
        self.assertEqual(platform_parameters.text, '')

        web_platform.click()
        sleep(2)
        self.assertEqual(platform_parameters.text, 'Web')

        ios_platform.click()
        sleep(2)
        self.assertEqual(platform_parameters.text, 'Web, iOS')

        android_platform.click()
        sleep(2)
        self.assertEqual(platform_parameters.text, 'Web, iOS, Android')

        custom_platform.click()
        sleep(2)
        self.assertEqual(platform_parameters.text, 'Web, iOS, Android, Custom')

        web_platform.click()
        sleep(2)
        self.assertEqual(platform_parameters.text, 'iOS, Android, Custom')

        android_platform.click()
        ios_platform.click()
        custom_platform.click()
        sleep(2)
        self.assertEqual(platform_parameters.text, '')

    def test_delivery_parameters(self):
        # check text near Delivery when choosing the radiobuttons

        browser = self.browser
        prototype = browser.find_element_by_xpath(self.prototype_xpath)
        mvp = browser.find_element_by_xpath(self.mvp_xpath)
        complete = browser.find_element_by_xpath(self.complete_xpath)
        existing = browser.find_element_by_xpath(self.existing_xpath)

        delivery_parameters = browser.find_element_by_xpath(self.delivery_parameters_xpath)
        self.assertEqual(delivery_parameters.text, '')

        prototype.click()
        sleep(2)
        self.assertEqual(delivery_parameters.text, 'Prototype')

        mvp.click()
        sleep(2)
        self.assertEqual(delivery_parameters.text, 'MVP')

        complete.click()
        sleep(2)
        self.assertEqual(delivery_parameters.text, 'Complete')

        existing.click()
        sleep(2)
        self.assertEqual(delivery_parameters.text, 'Existing')

        prototype.click()
        sleep(2)
        self.assertEqual(delivery_parameters.text, 'Prototype')

    def test_budget_range(self):
        # check text near Budget Range when choosing the radiobuttons

        browser = self.browser
        ten = browser.find_element_by_xpath(self.ten_xpath)
        twentyfive = browser.find_element_by_xpath(self.twentyfive_xpath)
        fifty = browser.find_element_by_xpath(self.fifty_xpath)
        hundred = browser.find_element_by_xpath(self.hundred_xpath)

        budget_range = browser.find_element_by_xpath(self.budget_range_xpath)
        self.assertEqual(budget_range.text, '')

        ten.click()
        sleep(2)
        self.assertEqual(budget_range.text, '$10K - $25K')

        twentyfive.click()
        sleep(3)
        self.assertEqual(budget_range.text, '$25K - $50K')

        fifty.click()
        sleep(2)
        self.assertEqual(budget_range.text, '$50K - $100K')

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        hundred.click()
        sleep(2)
        self.assertEqual(budget_range.text, '$100K - $200K+')

        ten.click()
        sleep(2)
        self.assertEqual(budget_range.text, '$10K - $25K')

    @classmethod
    def tearDown(cls):
        cls.browser.quit()