from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get("https://arc.dev/remote-jobs")

page_content = page.content

soup = BeautifulSoup(page_content, 'lxml')

# print(soup.prettify())

my_div = soup.find("div", class_="sc-ba46ca07-0 dROrNK job-card")

# company_name = my_div.find("div", class_="company-name").text

# job_title = my_div.find("a", class_="job-title").text

job_link = my_div.find("a", class_="job-title")['href']

# print(f"https://arc.dev/remote-jobs{job_link}")

my_divs = soup.find_all("div", class_="sc-ba46ca07-0 dROrNK job-card")

company_names = []
job_titles = []

job_links = []
job_locations = []
job_salaries = []

for my_div in my_divs:
    company_names.append(my_div.find("div", class_="company-name").text)
    job_titles.append(my_div.find("a", class_="job-title").text)
    
    job_links.append(f"https://arc.dev/remote-jobs{my_div.find('a', class_='job-title')['href']}")
    

for job_link in job_links:
    page_two = requests.get(job_link)
    page_two_content = page_two.content
    soup_two = BeautifulSoup(page_two_content, 'lxml')
    
    my_div_two = soup_two.find("div", class_="sc-a9bceba6-0 dtrGJF")
    
    job_location = my_div_two.find("div", class_="sc-b9ad719a-0 jzcFMg").div.div.span.text
    job_locations.append(job_location)
    
    job_salary = my_div_two.find("div", class_="sc-b9ad719a-0 eSLzbJ").div.div.span.text
    job_salaries.append(job_salary)
    



my_data = {
    "Company Name": company_names,
    "Job Title": job_titles,
    "Job Location": job_locations,
    "Job ٍSalary": job_salaries
}

df = pd.DataFrame(my_data)

df.to_csv("jobs.csv",  index=False)

