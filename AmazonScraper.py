import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Duex-Portable-Lightweight-Brightness-Adjustable/dp/B07TDDSJ93/ref=sr_1_3?crid' \
      '=13J7TBMU44MZZ&dchild=1&keywords=duex+pro+portable+monitor&s=electronics&sprefix=duex+pro+p%2Celectronics' \
      '%2C171&sr=1-3 '

headers = {'authority': 'www.amazon.com',
           'pragma': 'no-cache',
           'cache-control': 'no-cache',
           'dnt': '1',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'sec-fetch-site': 'none',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-dest': 'document',
           'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

price = soup.find(id="priceblock_saleprice").get_text()
print(price)

# print(soup.prettify())
