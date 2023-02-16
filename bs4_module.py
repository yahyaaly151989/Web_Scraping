# =========================== BeautifulSoup4 Module =================================
# pip/pip3 install beautifulsoup4
# pip/pip3 install bs4
# python -m pip install beautifulsoup4
# python -m pip3 install beautifulsoup4

# pip install lxml

import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

# with open("index.html", "r") as html_file:
    
#     # content = html_file.read()
    
#     my_page = BeautifulSoup(html_file, "lxml")
    
#     # print(my_page)
#     # print(my_page.prettify())
    
#     page_title = my_page.title
    
#     # print(page_title)
#     # print(page_title.string)
#     # print(page_title.text)
    
#     # my_h2 = my_page.h2
    
#     # print(my_h2)
    
#     # my_div = my_page.find("div")
    
#     # print(my_div)
    
#     # my_divs = my_page.find_all("div", {"class": "css-content"})
#     my_divs = my_page.find_all("div", class_="css-content")
    
#     # print(my_divs)
    
#     # my_div_titles = my_page.find_all("h2")
    
#     # for my_div_title in my_div_titles:
#     #     print(my_div_title.text)
    
#     my_div_links = my_page.find_all("a")
    
#     # print(my_div_links)
    
#     for my_div_link in my_div_links:
#         print(my_div_link["href"])

def find_jobs():
    r = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text


    content = BeautifulSoup(r, "lxml")

    jobs = content.find_all("li", class_="clearfix job-bx wht-shd-bx")

    job_titles = []
    company_names = []
    company_locations = []
    jobs_skills = []
    published_dates = []
        
    for job in jobs:
        job_titles.append(job.find("a").text.strip())
        company_names.append(job.find("h3", class_="joblist-comp-name").text.strip())
        company_locations.append(job.find("ul", class_="top-jd-dtl clearfix").text.split()[-1])
        jobs_skills.append(job.find("span", class_="srp-skills").text.replace(" ", ""))
        published_dates.append(job.find("span", class_="sim-posted").text.replace("Posted ", ""))


    my_jobs = {
        "Job Title": job_titles,
        "Company Name": company_names,
        "Company Location": company_locations,
        "Job Skills": jobs_skills,
        "Published Date": published_dates,
    }

    df = pd.DataFrame(my_jobs)

    df.to_csv("jobs.csv", index=False)

if __name__ == "__main__":
    
    if True:
        find_jobs()
        
        time.sleep(600)
    