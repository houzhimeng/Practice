import requests
import uuid
from bs4 import BeautifulSoup

jav = requests.get('https://www.javbus.com')
print(jav.text)