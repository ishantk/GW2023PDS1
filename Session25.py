# Web Scrapping :)
# pip install beautifulsoup4
# pip install requests

import requests
from bs4 import BeautifulSoup

# url = "https://www.indiatoday.in/sports"
url = "https://www.indiatoday.in/health"
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
# print(type(soup), id(soup))
# print(soup.prettify())

# tags = soup.find_all("h3")
tags = soup.find_all("div", class_="B1S3_content__wrap__9mSB6")
for tag in tags:
    print("````````````````````````````")
    print(tag.text)
    print("````````````````````````````")
    print()