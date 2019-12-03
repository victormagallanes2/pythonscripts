from seleniumrequests import Chrome
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver
from seleniumrequests import Chrome

chrome_options = Options()
chrome_options.add_argument("--headless")

navegator = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'/home/victor/programas/chromedriver')
navegator.request('GET','https://jsonplaceholder.typicode.com/users')

first_request = navegator.requests[0]
if first_request:
    print(
    	first_request.method,
        #first_request.path,
        #first_request.response.status_code
        first_request.response.status_code,
        first_request.response.reason,
        #first_request.response.headers,
        #first_request.response.body
    )
