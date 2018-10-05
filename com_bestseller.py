import requests
from bs4 import BeautifulSoup as soup
import csv
mydata = []
for i in range(1, 6):
    p = "https://www.amazon.com/best-sellers-books-Amazon/zgbs/" \
        "books/ref=zg_bs_pg_2?_encoding=UTF8&pg={}"
    r = requests.get(p.format(i))
    mysoup = soup(r.content, "html.parser")
    y = mysoup.find("div", {"id": "zg_centerListWrapper"})
    x = y.findAll("div", {"class": "zg_itemImmersion"})
    for item in x:
        try:
            name = item.find("img")['alt']
        except:
            name = "Not available"
        try:
            ufind = item.find("a", {"class": "a-link-normal"})['href']
            un = "www.amazon.in" + ufind
            url = un
        except:
            url = "Not available"
        try:
            author = item.find(
                "div", {"class": "a-row a-size-small"}).text.strip()
        except:
            author = "Not available"
        try:
            price = item.find("span", {"class": "p13n-sc-price"}).text.strip()
        except:
            price = "Not available"
        try:
            average = item.find("span", {"class": "a-icon-alt"}).text.strip()
            if average == "Prime":
                average = "Not available"
        except:
            average = "Not available"
        try:
            number = item.find(
                "a", {"class": "a-size-small a-link-normal"}).text
        except:
            number = "Not available"
        info = (name, url, author, price, number, average)
        mydata.append(info)
header = ("Name", "URL", "Author", "Price",
          "Number of Ratings", "Average Rating")
with open("output/com_book.csv", "w") as f:
    writer = csv.writer(f, delimiter=";", quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)
    writer.writerows(mydata)
