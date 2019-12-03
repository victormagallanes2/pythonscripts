from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from seleniumwire import webdriver

driver = webdriver.Chrome(executable_path=r'/home/victor/programas/chromedriver')
driver.get("https://kms.kinesis.money/login");
#time.sleep(10)
driver.find_element_by_id("input-login-email").send_keys("victormagallanes2@gmail.com")
driver.find_element_by_id ("input-login-password").send_keys("v181652981987")
driver.find_element_by_class_name('login-form__submit').click()

# driver.scopes = [
#     '.*stackoverflow.*',
#     '.*github.*'
# ]

for request in driver.requests:
    if request.response:
        print(
            request.path,
            request.response.status_code,
            request.response.headers['Content-Type']
        )