from seleniumrequests import Chrome
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")


webdriver = Chrome(chrome_options=chrome_options, executable_path=r'/home/victor/programas/chromedriver')
response = webdriver.request('GET', 'https://jsonplaceholder.typicode.com/users')
print(response)
