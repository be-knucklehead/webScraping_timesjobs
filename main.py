from bs4 import BeautifulSoup
import requests

print("Put some skill that you are familiar with")
familiar_skill = input(">")
print(f"Filtering out {familiar_skill}")


url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
http_content = requests.get(url)
http_text = http_content.text
soup = BeautifulSoup(http_text, "lxml")

jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

for job in jobs:
    post_date = job.find('span', class_="sim-posted").text
    if "few" in post_date:
        company_name = job.find('h3', class_="joblist-comp-name").text.replace(" ", "")
        skills = job.find('span', class_="srp-skills").text.replace(" ", "")
        job_link = job.header.h2.a['href']
        if familiar_skill in skills:
            print(f"Company Name: {company_name.strip()}")
            print(f"Required Skills: {skills.strip()}")
            print(f"More info: {job_link}")
