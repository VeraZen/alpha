import unittest
from selenium.webdriver import ActionChains
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

    #web_platform_xpath = "//input[@name='platform'][@value='Web']"
    #ios_platform_xpath = "//input[@name='platform'][@value='iOS']"
    #android_platform_xpath = "//input[@name='platform'][@value='Android']"
    #custom_platform_xpath = "//input[@name='platform'][@value='Custom']"

    #platform_parameters_xpath = "//p[@class='js-checkbox-params']/span"

    @classmethod
    def setUp(cls):
        cls.browser = webdriver.Chrome(chrome_driver_path)
        cls.browser.implicitly_wait(30)
        cls.browser.maximize_window()
        #basic https authentication login-djangostars, pass-ds2015
        cls.browser.get('https://djangostars:ds2015@beta.ds.inprogress.rocks/get-in-touch/')

    def test_delivery_parameters_hover(self):
        #check text near Platform when choosing the checkboxes

        browser = self.browser
        web_platform = browser.find_element_by_xpath(self.web_platform_xpath)

        sleep(5)
        ActionChains(browser).move_to_element(web_platform).perform()

        sleep(5)
        hover_color=browser.find_element_by_xpath("//div[@class='switch params web box']/label").value_of_css_property('color')


        self.assertEqual(hover_color, 'rgba(118, 189, 29, 1)')



        #self.assertEqual(greeting_1.text, 'THANK YOU FOR YOUR FEEDBACK')
        #self.assertEqual(greeting_2.text, "We'll reply you as soon as possible ;)")
    @classmethod
    def tearDown(cls):
        cls.browser.quit()