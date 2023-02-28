from bs4 import BeautifulSoup
import requests

url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
http_content = requests.get(url)
http_text = http_content.text
soup = BeautifulSoup(http_text, "lxml")

jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

for job in jobs:
    post_date = soup.find("span", class_="sim-posted")
    print(post_date)
