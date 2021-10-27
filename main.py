import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url='https://www.newegg.com/p/pl?d=graphic+card'

#opening up a connection and grabbin the page
uclient=ureq(my_url)
page_html=uclient.read()#store the raw html of the url in a variable
uclient.close()

#html parsing
page_soup=soup(page_html,"html.parser")
# page_soup.h1

products=page_soup.find_all("div",{"class":"item-cell"})
print(len(products))
print(" -------------")
# product=products[0]
# p=product.find_all("a",{"class":"item-title"})
# p["title"]

filename='products.csv'
f=open(filename,"w")
header='Brand, Product_name, Price, Shipping_status\n'
f.write(header)

for product in products:
    try:
        brand=product.div.div.div.a.img["title"]#main
        product_title=product.find_all("a",{"class":"item-title"})
        title_product=product_title[0]
        product_name=title_product.text#main
        shipping_status=product.find_all("li",{"class":"price-ship"})
        shipping_status=shipping_status[0].text#main
        curent_price=product.find_all("li",{"class":"price-current"})
        price=curent_price[0].text#main

        print("brand:  " + brand)
        print("product_name:  " + product_name)
        print("price:  " + price)
        print("shipping_status:  "   +shipping_status)
        print(" -------------")
        f.write(brand +  "," + product_name.replace(",","|") +  "," + price.replace("–","").replace(",","") +  "," + shipping_status + "\n" )

    

    except (TypeError, IndexError,AttributeError) as E:  # specific exceptions
        pass


f.close()
