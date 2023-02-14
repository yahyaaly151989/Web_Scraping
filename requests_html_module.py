# ======================== Requests-HTML Module ========================

# BeautifulSoup4
# Selenium
# Scrapy
# Requests-HTML

# =======================================================

from requests_html import HTML

with open("index.html", "r") as html_file:
    src = html_file.read()
    html = HTML(html=src)
    
# print(html.html)
# print(html.text)

# title = html.find("title")

# print(title[0].html)
# print(title[0].text)

# title = html.find("title", first=True)

# print(title.html)
# print(title.text)
my_posts = html.find(".css-content")

post_titles = []
post_descriptions = []
post_links = []

for my_post in my_posts:
    post_title = my_post.find("h2", first=True).text
    post_description = my_post.find("p", first=True).text
    post_link = list(my_post.find("a", first=True).links)[0]
    
    post_titles.append(post_title)
    post_descriptions.append(post_description)
    post_links.append(post_link)
    
print(post_titles)
print(post_descriptions)
print(post_links)