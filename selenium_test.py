from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/home/ali/Downloads/chromedriver-linux64/chromedriver'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
