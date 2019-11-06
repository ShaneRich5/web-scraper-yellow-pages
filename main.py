import requests
from bs4 import BeautifulSoup


url = 'https://www.yellowpages.com/washington-dc/mip/fti-consulting-541022726'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

main_header_element = soup.find('header', {'id': 'main-header'})
title_element = main_header_element.find('div', {'class': 'sales-info'})
address_element = main_header_element.find('h2', {'class': 'address'})
phone_element = main_header_element.find('p', {'class': 'phone'})

title = title_element.text
address = address_element.text
phone = phone_element.text

print('title:', title)
print('address:', address)
print('phone:', phone)