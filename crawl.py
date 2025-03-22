import requests
from bs4 import BeautifulSoup


url = "https://pecup.in"

response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
print(soup)