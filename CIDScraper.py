import requests
from bs4 import BeautifulSoup

URL = 'http://www.cidsanitary.com/catalog/'
URL2 = 'https://www.cidsanitary.com/catalog/Category/JMTDEO/Chemicals/Air-Freshner/'
URL3 = 'https://www.cidsanitary.com/catalog/Items/JMTDAE/Chemicals/Air-Freshner/Aerosol-Deodorant/'
URL4 = 'https://www.cidsanitary.com/catalog/g/CLAAFXXXXX/Claire-Handheld-Air-Fresheners/'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}

page = requests.get(URL)
page2 = requests.get(URL2)
page3 = requests.get(URL3)
page4 = requests.get(URL4)

soup = BeautifulSoup(page.text, 'html.parser')
soup2 = BeautifulSoup(page2.text, 'html.parser')
soup3 = BeautifulSoup(page3.text, 'html.parser')
soup4 = BeautifulSoup(page4.text, 'html.parser')

# for a in soup.findAll('a', href=True):
#    print(a['href'])

# for a in soup2.findAll('a', href=True):
#    print(a['href'])

# for a in soup3.findAll('a', href=True):
#    print(a['href'])

print(soup4.prettify())
for i in range(4):
    itemNum = soup4.find(id="ctl00_ctl00_cphMainContent_cphMainContent_ctl00_"
                            "Detail_Main_ctlSubItems_lvItems_ctrl" + str(i) + "_lblItem_No").get_text()
    print(itemNum)

# janitorialCategories = soup.findAll(class_="category-name")
# for i in range(len(janitorialCategories)):
#    print(f"Category {i+1}: {janitorialCategories[i]}")
