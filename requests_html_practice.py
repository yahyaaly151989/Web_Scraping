# ======================== Requests-HTML Module Practice ========================

from requests_html import HTMLSession

session = HTMLSession()

r = session.get("http://books.toscrape.com")

# print(r.status_code)

# book_category = r.html.find("#default > div > div > div > aside > div.side_categories > ul > li > ul > li:nth-child(1)", first=True)

# # print(book_category)
# # print(book_category.html)
# # print(book_category.text)

# book_category_link = list(book_category.absolute_links)[0]
# book_category_title = book_category.text

# print(book_category_link)
# print(book_category_title)

book_category_links = []

book_category_titles = []
book_names = []
book_prices = []
book_stocks = []
# book_descriptions = []

book_categories = r.html.find("#default > div > div > div > aside > div.side_categories > ul > li > ul > li")

for book_category in book_categories:
    book_category_titles.append(book_category.text)
    book_category_links.append(list(book_category.absolute_links)[0])
    
for book_category_link in book_category_links:
    r = session.get(book_category_link)

    book_infos = r.html.find("#default > div > div > div > div > section > div:nth-child(2) > ol > li")

    for book_info in book_infos:
        book_url = list(book_info.absolute_links)[0]
        r = session.get(book_url)
        book_name = r.html.find("#content_inner > article > div.row > div.col-sm-6.product_main > h1", first=True).text
        book_price = r.html.find("#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color", first=True).text
        book_stock = r.html.find("#content_inner > article > div.row > div.col-sm-6.product_main > p.instock.availability", first=True).text
        # book_description = r.html.find("#content_inner > article > p", first=True).text

        book_names.append(book_name)
        book_prices.append(book_price)
        book_stocks.append(book_stock)
        # book_descriptions.append(book_description)


# print(len(book_names))
# print(len(book_prices))
# print(len(book_stocks))
my_books = {
    "Book Name": book_names,
    "Book Price": book_prices,
    "Book Stock": book_stocks,
}

import pandas as pd

df = pd.DataFrame(my_books)

df.to_csv("myBooks.csv", index=False)