from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.aliexpress.com/item/1005004406776322.html').text
soup = BeautifulSoup(html_text, 'lxml')

shipping_cost = soup.find_all('div', class_='dynamic-shipping-line dynamic-shipping-titleLayout')

print(shipping_cost)
