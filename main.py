from bs4 import BeautifulSoup
import requests
import time

print("Put some skill that you are familiar with")
familiar_skill = input(">")
print(f"Filtering out {familiar_skill}")


def find_jobs():
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
    http_content = requests.get(url)
    http_text = http_content.text
    soup = BeautifulSoup(http_text, "lxml")

    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    for index, job in enumerate(jobs):
        post_date = job.find('span', class_="sim-posted").text
        if "few" in post_date:
            company_name = job.find('h3', class_="joblist-comp-name").text.replace(" ", "")
            skills = job.find('span', class_="srp-skills").text.replace(" ", "")
            job_link = job.header.h2.a['href']
            if familiar_skill in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()}")
                    f.write(f"Required Skills: {skills.strip()}")
                    f.write(f"More info: {job_link}")
                print('File saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
