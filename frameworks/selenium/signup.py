import unittest
from selenium import webdriver
import time
import requests
#from selenium.webdriver.common.keys import Keys

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'/home/victor/programas/chromedriver')


    # def test_signup_api(self):
        #driver = self.driver
        # driver.get("http://www.python.org")
        # url = 'https://uat-api.kinesis.money/api/accounts'
        # myobj = { "email": "victormagallanes3@gmail.com",
        #           "password": "v181652981987"
        #          }        
        # r = requests.post(url, data= myobj)
        # print(r.status_code)

    def test_signup(self):
        driver = self.driver
        driver.get("https://kms.kinesis.money/signup")
        driver.find_element_by_id("input-sign-up-email").send_keys("victormagallanes4@gmail.com")
        driver.find_element_by_id("input-sign-up-password").send_keys("v181652981987M")       
        driver.find_element_by_id("input-sign-up-password-retype").send_keys("v181652981987M")       
        driver.execute_script("document.querySelector('#termsOfServiceAgreement').click();") 
        driver.execute_script("document.querySelector('#privacyPolicyAgreement').click();") 
        driver.find_element_by_class_name('signup-form__submit').click()
        time.sleep(20)

    # def test_login_api(self):
        #driver = self.driver
        # driver.get("http://www.python.org")
        # url = 'https://uat-api.kinesis.money/api/sessions'
        # myobj = { "email": "victormagallanes3@gmail.com",
        #           "password": "v181652981987"
        #          }        
        # r = requests.post(url, data= myobj)
        # print(r.status_code)

    # def test_login(self):
    #     driver = self.driver
    #     driver.get("https://kms.kinesis.money/login")
    #     driver.find_element_by_id("input-login-email").send_keys("victormagallanes2@gmail.com")
    #     driver.find_element_by_id ("input-login-password").send_keys("v181652981987M")
    #     driver.find_element_by_class_name('login-form__submit').click()
    #     print(driver)
    #     time.sleep(20)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()