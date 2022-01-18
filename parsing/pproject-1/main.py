# pip i beautifulsoup lxml
from bs4 import BeautifulSoup

with open('pricing/index.html') as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, "lxml")

# t = soup.title
# print(t.text)
# print(t.string)

# link1_a = soup.find('a')
# print(link1_a)

# link2_a = soup.find_all('a')
# print(link2_a)
#
# for item in link2_a:
#     print(item.text)

# pr_desc1 = soup.find('p', class_='fs-5 text-muted')
# print(pr_desc1.text)
#
# pr_desc2 = soup.find('p', class_='fs-5 text-muted').text
# print(pr_desc2)
#
# pr_desc3 = soup.find(class_='fs-5 text-muted').text
# print(pr_desc3)
#
# tarifpro = soup.find('h4',{'class':'my-0 fw-normal', 'id':'001'}).text
# print(tarifpro)

tarifs = soup.find('main').find_all('h4')
# tarifs = soup.find_all('h4')
print(tarifs)
for i in tarifs:
    print(i.text)

price = soup.find_all('h1', class_ = 'pricing-card-title')
print(price)
for i in price:
    print(i.text)