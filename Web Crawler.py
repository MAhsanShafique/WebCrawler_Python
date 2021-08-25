import time

import requests
from bs4 import BeautifulSoup
import csv
familiar_skills = input("Enter skills that you are familiar with: ")
print(f"Filtering Out {familiar_skills}")

def find_job():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35'
    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html5lib')
    jobs = soup.findAll('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'today' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_details = job.header.h2.a['href']
            if familiar_skills in skills:
                with open(f'scrap result/{index}.txt', 'w') as f:
                    f.write(f"Company name : {company_name.strip()}\nRequired Skills : {skills.strip()}\n")
                    f.write(f"More Datail : {more_details}")
                print(f"FIle Saved: {index}")

if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f"Waiting {time_wait} minutes... ")
        time.sleep(time_wait * 60)